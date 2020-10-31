import random
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    model for user informations
    """
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_director = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    push_notification = models.BooleanField(
        default=True, help_text="Does the user wants push notifications from Infytrip?"
    )
    gender = models.CharField(max_length=30, default='', blank=True, null=True, help_text="Gender of user")
    dob = models.DateField(blank=True, null=True, help_text="Date of birth of user")
    nationality = models.CharField(max_length=100, blank=True, null=True, default='', help_text="Nationality of user")
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email


class ActivityLog(models.Model):
    """
    model to store user activity logs
    """
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='activity', blank=True, null=True,
        help_text="User to whom activity belongs to."
    )
    method = models.CharField(max_length=20, help_text="Request method get post put or patch")  # use get post put patch
    data = models.JSONField(help_text="Query parameters and request body data")  # query_params in get request and data in post
    url_path = models.TextField(help_text="Url requested")
    status_code = models.CharField(max_length=10, default='0', help_text="Status code returned from server")
    device_used = models.TextField(default='', help_text="Deviced used by user to request")
    ip_address = models.CharField(default='', max_length=255, help_text="IP address of user")
    browser_used = models.TextField(default='', help_text="Browser used by user")
    accessed_at = models.DateTimeField(auto_now_add=True)