from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    department_location = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name