from django.db import models

# Create your models here.
class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    appointment_date = models.DateField()
    patient_id = models.ForeignKey('user.Patient', on_delete=models.CASCADE)
    doctor_id = models.ForeignKey('user.Doctor', on_delete=models.CASCADE)
    appointment_status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.patient_id} - {self.doctor_id}"
