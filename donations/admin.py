from django.contrib import admin
from .models import (
    Causes,
    CausesDonation,
    ProjectDonation,
    Transaction,
)
import csv
from django.http import HttpResponse
# Register your models here.

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class CauseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }


class DonationAdmin(admin.ModelAdmin, ExportCsvMixin):
    readonly_fields = ('status', 'method','donation_id', )
    list_filter = ('method', 'status', )
    list_display = ('first_name', 'last_name', 'method', 'status', 'amount',)
    actions = ('export_as_csv', )

    def get_readonly_fields(self, request, obj=None):

        if hasattr(obj, 'method') and obj.method=='offline':
            return ['method', 'donation_id', ]
        else:
            return self.readonly_fields 


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'padded_card_no', 'response_code', 'reason_code_desc', 'auth_code', 'currency',)

    search_fields = ('order_id',)

    readonly_fields = (
        'order_id', 'response_code', 'reason_code', 'reason_code_desc',
        'reference_no', 'padded_card_no', 'auth_code', 'cvv2_result',
        'original_response', 'signature',
    )

admin.site.register(Causes, CauseAdmin)
admin.site.register(CausesDonation, DonationAdmin)
admin.site.register(ProjectDonation, DonationAdmin)
admin.site.register(Transaction, TransactionAdmin)