from django.db import models
from django.utils import timezone
from django.conf import settings
from common import views
from django.core.mail import send_mail

# Create your models here.
class MicoModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(blank=True, null=True)

    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.pk:
            self.created_at = now
        self.updated_at = now
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        now = timezone.now()
        self.deleted_on = now
        self.is_deleted = True
        super().save()
    """


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.TextField()

    def __str__(self):
        return self.subject

    def send(self, request):
        subscribers = Subscriber.objects.all()
        for sub in subscribers:
            send_mail(
                from_email="info@themicofoundationja.com",
                recipient_list=[sub.email, ],
                message = '',
                subject=self.subject,
                html_message=self.contents,
                fail_silently=True,
                )


class EmailSetting(models.Model):
    email_use_tls = models.BooleanField(default=True)
    email_host = models.CharField(max_length=1024)
    email_host_user = models.CharField(max_length=255)
    email_host_password = models.CharField(max_length=255)
    email_port = models.PositiveSmallIntegerField(default=587)

    def __str__(self):
        return "Click here to edit SMTP settings"