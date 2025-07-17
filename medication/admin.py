from django.contrib import admin
from .models import Medication

# Register your models here.
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('medication_name', 'medication_description', 'medication_side_effects')

admin.site.register(Medication, MedicationAdmin)