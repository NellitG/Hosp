from django.db import models

# Create your models here.
class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    treatment_id = models.ForeignKey('treatment.Treatment', on_delete=models.CASCADE, related_name='prescriptions')
    medication_id = models.ForeignKey('medication.Medication', on_delete=models.CASCADE, related_name='prescriptions')
    dosage = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return str(self.prescription_id)