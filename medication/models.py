from django.db import models

# Create your models here.
class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    medication_name = models.CharField(max_length=255)
    medication_description = models.TextField()
    medication_side_effects = models.TextField()

    def __str__(self):
        return self.medication_name