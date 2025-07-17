from django.db import models

# Create your models here.
class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey('user.Patient', on_delete=models.CASCADE)
    treatment_id = models.ForeignKey('treatment.Treatment', on_delete=models.CASCADE)
    bill_amount = models.IntegerField()
    bill_date = models.DateField()
    bill_method = models.CharField(max_length=20, choices=[('Pending', 'Pending'),  ('completed', 'Completed')])

    def __str__(self):
        return f"{self.bill_date} - {self.bill_amount}"