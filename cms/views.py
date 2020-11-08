import datetime
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from .forms import ContactForm, EndowmentForm, WorkwithusForm, SponsorshipForm
from .models import (
    NewsPost,
    BOD,
    Resource,
    Team,
    Slider,
    Project,
    Event,
    Work,
    Message,
    MissionValue,
    Event,
    History,
    FAQ,
    Trustee,
    Popup,
    Gallery,
    HomepageManagement,
    WorkWithUs,
    Sponsorship,
    GetInvolvedImage,
    Policy,
)
from donations.models import Causes, CausesDonation, ProjectDonation
from django.db.models import Sum
from donations.fac import msTimeStamp, authorize
from django.http import HttpResponseRedirect
from django.contrib import messages
from common.models import Subscriber
from django.core.mail import send_mail
from django.conf import settings
from common.views import email_backend
import datetime
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def homepage(request):
    sliders = Slider.objects.all()
    popups = Popup.objects.all()
    
    homepage_content = HomepageManagement.objects.first()
    events = Event.objects.filter(date__date__gte=datetime.datetime.now())
    if request.method == 'POST':
        sub, created = Subscriber.objects.get_or_create(email=request.POST['email'], defaults={'first_name': request.POST['firstName'], 'last_name': request.POST['lastName'],})
        sub.save()
        send_mail(
            from_email="info@themicofoundationja.com",
            recipient_list=[sub.email, ],
            subject='Mico Foundation Mailing List Confirmation',
            message='Thank you for signing up for MICO Foundation mailing list!',
            fail_silently=True,
            )
        if created:
            messages.add_message(request, messages.INFO, 'Successfully Subscribed')
        else:
            messages.add_message(request, messages.INFO, 'Email Already Exist')
    return render(request, 'index.html', {
        'sliders': sliders,
        'events': events,
        'popups': popups,
        'homepage_content': homepage_content,
    })


def aboutpage(request):
    works = Work.objects.all()
    return render(request, 'aboutus.html', {
        'works': works,
    })


def causesview(request):
    causes = Causes.objects.all().annotate(sum=Sum('causedonation__amount'))
    return render(request, 'causes.html', {
        'causes': causes,
    })


def directorview(request):
    directors = BOD.objects.all()
    context = {'directors': directors}
    return render(request, 'director.html', context)


def historyview(request):
    directors = History.objects.filter(is_director=True).order_by('-start_year')
    chairmans = History.objects.filter(is_chairman=True).order_by('-start_year')
    secretaries = History.objects.filter(is_secretary=True).order_by('-start_year')
    context = {
        'directors': directors,
        'chairmans': chairmans,
        'secretaries': secretaries,
    }
    return render(request, 'history.html', context)


def sponsorship(request):
    form = SponsorshipForm()
    context = {'form':form}
    if request.method == 'POST':
        form = SponsorshipForm(request.POST)

        if form.is_valid():
            email=form.cleaned_data.get('email')
            form.save()
            send_mail(
                from_email="info@themicofoundationja.com",
                recipient_list=[email, ],
                subject='Thank you for sponsorship',
                message='Thank you for sponsoring MICO Foundation!',
                fail_silently=True,
            )
            redirect('contact')
            messages.add_message(request, messages.SUCCESS, "Successfully Submitted the form.")
        else:
            return render(request, 'sponsorship.html', context)
    else:
        return render(request, 'sponsorship.html', context)
    return render(request, 'sponsorship.html', context)


def contact(request):
    form = ContactForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email_address')
            form.save()
            send_mail(
                from_email="info@themicofoundationja.com",
                recipient_list=[email, ],
                subject='Thank you for contacting',
                message='Thank you for contacting MICO Foundation!',
                fail_silently=True,
            )
            form.save()
            redirect('contact')
            messages.add_message(request, messages.SUCCESS, "Successfully Submitted the form.")
        else:
            return render(request, 'contact.html', context)

    else:
        return render(request, 'contact.html', context)

    return render(request, 'contact.html', context)


def message(request):
    messages = Message.objects.all()
    return render(request, 'message.html', {
        'messages': messages,
    })


def message_detail(request, slug):
    message = get_object_or_404(Message, slug=slug)
    return render(request, 'messagedetail.html', {
        'message': message,
    })


def newsroom(request):
    news = NewsPost.objects.all().order_by('-date')[:2]
    carousel_news = NewsPost.objects.all().order_by('-date')[2:]
    context = {
        'news':news,
        'carousel_news': carousel_news,
    }
    return render(request, 'newsroom.html', context)


def missionview(request):
    values = MissionValue.objects.all()
    return render(request, 'mission.html', {
        'values': values,
    })


def resources(request):
    resources = Resource.objects.filter(access_level='Public')
    context = {'resources' : resources}
    return render(request, 'resource.html', context)


def trustees(request):
    trustees = Trustee.objects.all()
    return render(request, 'trustees.html', {
        'trustees':trustees,
    })


def workwithus(request):
    form = WorkwithusForm()
    context = {'form':form}
    if request.method == 'POST':
        form = WorkwithusForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            form.save()
            send_mail(
                from_email="info@themicofoundationja.com",
                recipient_list=[email, ],
                subject='Thank you for sponsorship',
                message='Thank you for sponsoring MICO Foundation!',
                fail_silently=True,
            )
            form.save()
            redirect('contact')
            messages.add_message(request, messages.SUCCESS, "Successfully Submitted the form.")
        else:
            return render(request, 'workwithus.html', context)
    else:
        return render(request, 'workwithus.html', context)
    return render(request, 'workwithus.html', context)


def staffs(request):
    teams = Team.objects.all()
    return render(request, 'staff.html', {
        'teams': teams,
    })


def event_view(request):
    latest = Event.objects.filter(date__gte=datetime.date.today()).order_by('date')
    if len(latest) > 0:
    	latest = latest.first()
    else:
    	latest = []
    events = Event.objects.all().order_by('-date')
    return render(request, 'events.html', {
        'events': events,
        'latest': latest,
    })

def endowment(request):
    form = EndowmentForm()
    faqs = FAQ.objects.all()
    context = {'form': form, 'faqs': faqs}
    if request.method == 'POST':
        form = EndowmentForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            form.save()
            send_mail(
                from_email="info@themicofoundationja.com",
                recipient_list=[email, ],
                subject='Thank you for donating endowment',
                message='Thank you for donating endowments to MICO Foundation!',
                fail_silently=True,
            )
            form.save()
            redirect('contact')
            messages.add_message(request, messages.SUCCESS, "Successfully Submitted the form.")
        else:
            return render(request, 'endowments.html', context)

    else:
        return render(request, 'endowments.html', context)

    return render(request, 'endowments.html', context)


def news_detail(request, slug):
    news = get_object_or_404(NewsPost, slug=slug)
    images = Gallery.objects.filter(news__id=news.id)
    try:
        next_post = news.get_next_by_date()
    except NewsPost.DoesNotExist:
        next_post = None

    try:
        previous_post = news.get_previous_by_date()
    except NewsPost.DoesNotExist:
        previous_post = None

    return render(request, 'newsdetail.html', {
        'news': news,
        'images': images,
        'previous_news': previous_post,
        'next_news': next_post,
    })


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'eventdetail.html', {
        'event': event,
    })


def work_detail(request, slug):
    work = get_object_or_404(Work, slug=slug)
    return render(request, 'workdetail.html', {
        'work': work,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projectdetail.html', {
        'project': project,
    })


def get_involved(request):
    projects = Project.objects.all()
    causes = Causes.objects.all()
    images = GetInvolvedImage.objects.all()
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
            Subscriber.objects.create(first_name=first_name, last_name=last_name, email=email)
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
    return render(request, 'getinvolved.html', {
        'projects': projects,
        'causes': causes,
        'images': images,
    })


@csrf_exempt
def update_content(request):
    donation_for = request.GET.get('donate_name', None)
    donation_for = str(donation_for).split(',')
    donation_type = donation_for[0]
    donation_id = donation_for[1]
    if donation_type == 'project':
        project = get_object_or_404(Project, id=donation_id)
        return render(request, 'project_body.html', {'project': project})
    else:
        cause = get_object_or_404(Causes, id=donation_id)
        return render(request, 'cause_body.html', {'cause': cause})


def terms_policy(request, slug):
    policy = get_object_or_404(Policy, type=slug.capitalize())

    return render(request, 'terms/terms.html', {
        'policy': policy,
    })
