from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    contact=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    msg=models.CharField(max_length=200)
    
    
    
