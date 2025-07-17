from django.db import models

# Create your models here.
class Treatment(models.Model):
    treatment_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey('user.Patient', on_delete=models.CASCADE, related_name='treatments')
    doctor_id = models.ForeignKey('user.Doctor', on_delete=models.CASCADE, related_name='treatments')
    treatment_date = models.DateField()
    treatment_diagnosis = models.CharField(max_length=255)
    treatment_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.treatment_date} - {self.treatment_diagnosis}"