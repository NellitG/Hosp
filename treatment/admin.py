from django.contrib import admin
from .models import Treatment

# Register your models here.
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatment_id', 'patient_id', 'doctor_id', 'treatment_date', 'treatment_diagnosis', 'treatment_notes')

admin.site.register(Treatment, TreatmentAdmin)