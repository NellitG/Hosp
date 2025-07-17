from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Create a model for abstract user with role choices
class CustomUser(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient'),
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def __str__(self):
        return self.name or self.username
    
class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department_id = models.ForeignKey('department.Department', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

  
    
class Nurse(models.Model):
    nurse_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    department_id = models.ForeignKey('department.Department', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    