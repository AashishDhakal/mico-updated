from django.contrib import admin
from .models import (
    Slider,
    NewsPost,
    Resource,
    Contact,
    Team,
    Trustee,
    Message,
    History,
    Event,
    Endowment,
    BOD,
    Work,
    Project,
    MissionValue,
    FAQ,
    Popup,
    Advertisement,
    Gallery,
    HomepageManagement,
    WorkWithUs,
    Sponsorship,
    ContentManagement,
    NewsCategory,
    GetInvolvedImage,
)

from django_summernote.admin import SummernoteModelAdmin
from djsingleton.admin import SingletonAdmin, SingletonActiveAdmin
# Register your models here.


from django_summernote.admin import SummernoteModelAdmin

# summernotes

class GalleryInlineAdmin(admin.TabularInline):
    model = Gallery


class NewsPostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }
    summernote_fields = ['description', ]
    inlines = [GalleryInlineAdmin, ]


class ResourceAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }
    summernote_fields = ['description', ]


class ContactAdmin(SummernoteModelAdmin):
    summernote_fields = ['message', ]


class TeamAdmin(SummernoteModelAdmin):
    summernote_fields = ['bio', ]


class TrusteeAdmin(SummernoteModelAdmin):
    summernote_fields = ['bio', ]


class MessageAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('message_by',),}
    summernote_fields = ['message', ]


class HistoryAdmin(SummernoteModelAdmin):
    summernote_fields = ['short_description', ]


class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }
    summernote_fields = ['description',]


class EndowmentAdmin(SummernoteModelAdmin):
    summernote_fields = ['description', ]


class BODAdmin(SummernoteModelAdmin):
    summernote_fields = ['bio', ]


class WorkAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }
    summernote_fields = ['detail', ]


class ProjectAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('project_name', ), }
    summernote_fields = ['detail', ]


class ContentAdmin(SummernoteModelAdmin):
    summernote_fields = ['endowment_text', 'sponsorship_who_we_are', 'history_description', 'about_description',
     'sponsorship_become_sponsor_text', 'workwithus_banner_text_1', 'workwithus_banner_text_2',
     ]


admin.site.register(Slider)
admin.site.register(NewsCategory)
admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Trustee, TrusteeAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Endowment, EndowmentAdmin)
admin.site.register(BOD, BODAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(MissionValue)
admin.site.register(FAQ)
admin.site.register(Popup)
admin.site.register(Advertisement)
admin.site.register(HomepageManagement)
admin.site.register(WorkWithUs)
admin.site.register(Sponsorship)
admin.site.register(ContentManagement, ContentAdmin)
admin.site.register(GetInvolvedImage)
