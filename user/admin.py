from django.contrib import admin
from user.models import CustomUser, Doctor, Nurse, Patient

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Nurse)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'date_of_birth', 'phone', 'email', 'address')
admin.site.register(Patient, PatientAdmin)