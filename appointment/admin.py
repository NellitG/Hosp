from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'appointment_date', 'patient_id', 'doctor_id', 'appointment_status')

admin.site.register(Appointment, AppointmentAdmin)