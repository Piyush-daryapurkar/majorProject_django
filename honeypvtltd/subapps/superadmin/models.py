from django.db import models

# Create your models here.

class Superadmin_data(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    
class Manager_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    birth_date=models.DateField()
    joining_date=models.DateField()
    emp_id=models.CharField(max_length=10)

