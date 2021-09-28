from django.db import models

# Create your models here.

class Cars(models.Model):
    carname = models.CharField(max_length=100)
    carcompany = models.CharField(max_length=20)
    driveline = models.CharField(max_length=20)
    geartype = models.CharField(max_length=20)