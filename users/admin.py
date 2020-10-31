from django.contrib import admin
from .models import (
    User,
    ActivityLog,
)

class ActivityLogAdmin(admin.ModelAdmin):
    search_fields = ['url_path',]
    list_filter = ['method', 'status_code',]

# Register your models here.
admin.site.register(User)
admin.site.register(ActivityLog, ActivityLogAdmin)