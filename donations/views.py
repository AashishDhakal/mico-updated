from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from .models import Causes, CausesDonation, ProjectDonation, Project, Transaction
from django.conf import settings
from django.shortcuts import reverse
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from .fac import msTimeStamp, authorize
import zeep
from zeep import Client
import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.db.models import Sum
from .forms import ExtPayPalPaymentsForm
from common.models import Subscriber
from django.core.mail import send_mail
from django.template.loader import render_to_string

from . import exceptions as error

# Create your views here.
def CauseView(request):
    causes = Causes.objects.all()
    return render(request, 'causes.html', {'causes': causes,})


def donate_view(request):
        projects = Project.objects.all()
        causes = Causes.objects.all()
        if request.POST:
            donation_for = request.POST['donateName']
            donation_for = str(donation_for).split(',')
            donation_type = donation_for[0]
            donation_id = donation_for[1]                
            amount = request.POST['donateAmount']
            if amount == 'other':
                amount = request.POST['customAmount']
            first_name = request.POST['firstName']
            last_name = request.POST['lastName']
            address_one = request.POST['addressOne']
            address_two = request.POST['addressTwo']
            if not address_two:
                address_two = ''
            email = request.POST['email']
            country = request.POST['country']
            postcode = request.POST['postcode']
            state = request.POST['state']
            city = request.POST['city']
            phone = request.POST['phone']
            subscribe = request.POST['subscribe']
            if subscribe == '1':
                Subscriber.objects.get_or_create(email=email, defaults={'first_name': first_name, 'last_name': last_name,},)
            if not phone:
                phone = ''
            method = request.POST['donatePaymentMethod']
            order_number = msTimeStamp()
            if [donation_for, amount, first_name, last_name, address_one, email, country, postcode, state, city, method ]:
                if donation_type == 'project':
                    project = get_object_or_404(Project, id=donation_id)
                    donation = ProjectDonation.objects.create(
                        project = project,
                        donation_id = order_number,
                        amount= amount,
                        first_name= first_name,
                        last_name= last_name,
                        address_line_1 = address_one,
                        address_line_2 = address_two,
                        city = city,
                        zip_code = postcode,
                        country = country,
                        email = email,
                        phone = phone,
                        method = method,
                        status = "Not Paid"
                    )
                else:
                    cause = get_object_or_404(Causes, id=donation_id)
                    donation = Causes.objects.create(
                        cause = cause,
                        donation_id = order_number,
                        amount= amount,
                        first_name= first_name,
                        last_name= last_name,
                        address_line_1 = address_one,
                        address_line_2 = address_two,
                        city = city,
                        zip_code = postcode,
                        country = country,
                        email = email,
                        phone = phone,
                        method = method,
                        status = "Not Paid"
                    )
            if method == 'card':
                cvv = request.POST['cvv']
                card_no = request.POST['cardNo']
                card_no = str(card_no).replace(" ", "")
                month = request.POST['Month']
                year = request.POST['Year']
                expiry = f'{month}{year}'
                amount = int(donation.amount) * 100
                amount = f"{amount:012d}"
                order_number = order_number
                result = authorize(cvv, expiry, card_no, amount, order_number)
                #messages.add_message(request,messages.INFO, result)
                return render(request, 'processcard.html', {'result': result,})
            elif method=='paypal':
                return redirect(f'{reverse("process_paypal")}?df={donation_type}&id={donation.uuid}')
            elif method=='offline':
                return render(request, 'offlinedonation.html', {})    
        return render(request, 'donate.html', {
            'projects': projects,
            'causes': causes,
        })


def project_donate(request, slug):
    project = Project.objects.annotate(sum=Sum('projectdonation__amount')).get(slug=slug)
    if request.POST:
        amount = request.POST['donateAmount']
        if amount == 'other':
            amount = request.POST['customAmount']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        address_one = request.POST['addressOne']
        address_two = request.POST['addressTwo']
        if not address_two:
            address_two = ''
        email = request.POST['email']
        country = request.POST['country']
        postcode = request.POST['postcode']
        state = request.POST['state']
        city = request.POST['city']
        phone = request.POST['phone']
        subscribe = request.POST['subscribe']
        if subscribe == '1':
            Subscriber.objects.get_or_create(email=email, defaults={'first_name': first_name, 'last_name': last_name,},)
        if not phone:
            phone = ''
        method = request.POST['donatePaymentMethod']
        order_number = msTimeStamp()
        if [amount, first_name, last_name, address_one, email, country, postcode, state, city, method ]:     
            project_donation = ProjectDonation.objects.create(
                project = project,
                donation_id = order_number,
                amount= amount,
                first_name= first_name,
                last_name= last_name,
                address_line_1 = address_one,
                address_line_2 = address_two,
                city = city,
                zip_code = postcode,
                country = country,
                email = email,
                phone = phone,
                method = method,
                status = "Not Paid"
            )
        if method == 'card':
            cvv = request.POST['cvv']
            card_no = request.POST['cardNo']
            card_no = str(card_no).replace(" ", "")
            month = request.POST['Month']
            year = request.POST['Year']
            expiry = f'{month}{year}'
            amount = int(project_donation.amount) * 100
            amount = f"{amount:012d}"
            order_number = order_number
            result = authorize(cvv, expiry, card_no, amount, order_number)
            #messages.add_message(request,messages.INFO, result)
            return render(request, 'processcard.html', {'result': result,})
        elif method=='paypal':
            return redirect(f'{reverse("process_paypal")}?df=project&id={project_donation.uuid}')
        elif method=='offline':
            return render(request, 'offlinedonation.html', {})   
    return render(request, 'projectdonate.html', {'project': project})


def causes_donate(request, slug):
    cause = Causes.objects.annotate(sum=Sum('causedonation__amount')).get(slug=slug)
    if request.POST:
        amount = request.POST['donateAmount']
        if amount == 'other':
            amount = request.POST['customAmount']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        address_one = request.POST['addressOne']
        address_two = request.POST['addressTwo']
        if not address_two:
            address_two = ''
        email = request.POST['email']
        country = request.POST['country']
        postcode = request.POST['postcode']
        state = request.POST['state']
        city = request.POST['city']
        phone = request.POST['phone']
        subscribe = request.POST['subscribe']
        if subscribe == '1':
            Subscriber.objects.get_or_create(email=email, defaults={'first_name': first_name, 'last_name': last_name,},)
        if not phone:
            phone = ''
        method = request.POST['donatePaymentMethod']
        order_number = msTimeStamp()
        if [amount, first_name, last_name, address_one, email, country, postcode, state, city, method ]:     
            cause_donation = CausesDonation.objects.create(
                cause = cause,
                donation_id = order_number,
                amount= amount,
                first_name= first_name,
                last_name= last_name,
                address_line_1 = address_one,
                address_line_2 = address_two,
                city = city,
                zip_code = postcode,
                country = country,
                email = email,
                phone = phone,
                method = method,
                status = "Not Paid"
            )
        if method == 'card':
            cvv = request.POST['cvv']
            card_no = request.POST['cardNo']
            card_no = str(card_no).replace(" ", "")          
            month = request.POST['Month']
            year = request.POST['Year']
            expiry = f'{month}{year}'
            amount = int(cause_donation.amount) * 100
            amount = f"{amount:012d}"
            order_number = order_number
            result = authorize(cvv, expiry, card_no, amount, order_number)
            #messages.add_message(request,messages.INFO, result)
            return render(request, 'processcard.html', {'result': result,})
        elif method=='paypal':
            return redirect(f'{reverse("process_paypal")}?df=cause&id={cause_donation.uuid}')
        elif method=='offline':
            return render(request, 'offlinedonation.html', {})   
    return render(request, 'causedonate.html', {'cause': cause})


def process_paypal(request):
    host = request.get_host()
    donate_for=request.GET.get('df', False)
    uuid = request.GET.get('id', False)
    if donate_for == 'cause' and uuid:
        donation = get_object_or_404(CausesDonation, uuid=uuid)
    elif donate_for == 'project' and uuid:
        donation = get_object_or_404(ProjectDonation, uuid=uuid)
    else:
        return HttpResponseRedirect(reverse('home'))
    if donation:
        paypal_dict = {
            "cmd": "_donations",
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': donation.amount,
            'invoice': str(donation.uuid),
            'item_name': '',
            'custom': f'{donate_for}',
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host,
                                            reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                            reverse('payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                reverse('payment_cancelled')),
        }
        form = ExtPayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'process_paypal.html', {'paypal_form': form})
    else:
        return HttpResponseRedirect(reverse('home'))


@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')

@csrf_exempt
def save_transaction(request):
    data = ''
    donation = None
    request.session.modified = True
    
    #request.session['donate_message'] = 'Some Error Message'
    #return HttpResponseRedirect(reverse('donate'))
    
    if request.POST:
        try:
            if u'OrderID' not in request.POST:
                raise error.PaymentError('Unable to process donation.')
            
            if   u'ReferenceNo' not in request.POST and int(request.POST['ResponseCode']) != 1:
                raise error.CardError(request.POST['ReasonCodeDesc'])

            order_id = request.POST['OrderID']
            response_code = request.POST['ResponseCode']
            reason_code = request.POST['ReasonCode']
            reason_code_desc = request.POST['ReasonCodeDesc']
            reference_no = request.POST['ReferenceNo']
            padded_card_no = request.POST['PaddedCardNo']
            auth_code = request.POST['AuthCode']
            cvv2_result = request.POST['CVV2Result']
            original_response = request.POST['OriginalResponseCode']
            signature = request.POST['Signature']
            data = reason_code_desc
            if [order_id, response_code, reason_code, reason_code_desc, reference_no, padded_card_no, auth_code, cvv2_result, original_response, signature]:
                Transaction.objects.create(
                    order_id=order_id,
                    response_code=response_code,
                    reason_code=reason_code,
                    reason_code_desc=reason_code_desc,
                    reference_no=reference_no,
                    padded_card_no=padded_card_no,
                    auth_code=auth_code,
                    cvv2_result=cvv2_result,
                    original_response=original_response,
                    signature=signature
                )
                try:
                    donation = CausesDonation.objects.get(donation_id=order_id)
                    if response_code == '1':
                        donation.status = 'Paid'
                    else:
                        donation.status = reason_code_desc
                    donation.save()
                except CausesDonation.DoesNotExist:
                    donation = ProjectDonation.objects.get(donation_id=order_id)
                    if response_code == '1':
                        donation.status = 'Paid'
                    else:
                        donation.status = reason_code_desc
                    donation.save()
            if donation:
                if donation.status == 'Paid':
                    send_mail(
                        subject="Mico Foundation Donation Receipt",
                        from_email="info@themicofoundationja.com",
                        recipient_list = [donation.email, ],
                        message = 'Donation Receipt',
                        html_message= render_to_string('donation_receipt.html', {
                            'donation': donation,
                        }),
                    )
        except error.CardError as e:
            request.session['donate_message'] = str(e)
            return HttpResponseRedirect(reverse('donate'))
        except error.PaymentError as e:
            request.session['donate_message'] = str(e)
            return HttpResponseRedirect(reverse('donate'))
        except Exception as e:
            request.session['donate_message'] = str(e)
            return HttpResponseRedirect(reverse('donate'))

    return render(request, 'transactionresult.html', {
        'data': data,
        'donation': donation,
    })
