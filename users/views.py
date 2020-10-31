
from django.shortcuts import render,reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout,password_validation
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignupForm
from common.views import email_backend

from cms.models import Resource

@login_required
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def LoginView(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user:
            if user.is_active:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.add_message(request,messages.INFO,'Account not active')
        else:
            messages.add_message(request,messages.INFO,'Invalid Login')
    return render(request, "login.html")


def SignupView(request):
    if request.method == 'POST' :
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password_validation.validate_password(user.password)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Mico Foundation account.'
            html_message = render_to_string('registration/acc_active_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                'token' : account_activation_token.make_token(user),
            })
            email = form.cleaned_data.get('email')
            to_email = [email]
            send_mail(from_email='info@themicofoundationja.com',subject=mail_subject,message='Activate your account',recipient_list=to_email,html_message=html_message)
            return render(request, 'registration/confirmemail.html')
    else:
        form = UserSignupForm()
    return render(request,'signup.html',{'form':form, })

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'registration/emailconfirmed.html')
    else:
        return render(request, 'registration/confirmationfailed.html')

def profile(request):
    loggedin_user = User.objects.get(id=request.user.id)
    if loggedin_user.is_director:
        resources = Resource.objects.filter(access_level='Directors Only')
    else:
        resources = None
    return render(request,'registration/profile.html',{
        'loggedin_user':loggedin_user,
        'resources': resources,
    })