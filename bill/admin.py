from django.contrib import admin
from .models import Bill

# Register your models here.
class BillAdmin(admin.ModelAdmin):
    list_display = ('bill_id', 'patient_id', 'treatment_id', 'bill_amount', 'bill_date', 'bill_method')

admin.site.register(Bill, BillAdmin)