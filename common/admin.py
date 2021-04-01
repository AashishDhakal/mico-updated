from django.contrib import admin
from .models import Subscriber, Newsletter, EmailSetting

from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

def send_mail(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)


send_mail.short_description = "Send selected mail to all subscribers"


class NewsletterAdmin(SummernoteModelAdmin):
    summernote_fields = ['contents', ]
    actions = [send_mail, ]


admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(EmailSetting)
