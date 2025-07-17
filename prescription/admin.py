from django.contrib import admin
from .models import Prescription

# Register your models here.
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('prescription_id', 'treatment_id', 'medication_id', 'dosage', 'duration')

admin.site.register(Prescription, PrescriptionAdmin)
