from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend


def email_backend():
    from common.models import EmailSetting
    config = EmailSetting.objects.first()

    backend = EmailBackend(host=config.email_host, port=config.email_port,
                           username=config.email_host_user,
                           password=config.email_host_password,
                           use_tls=config.email_use_tls, fail_silently=True)
    return backend
