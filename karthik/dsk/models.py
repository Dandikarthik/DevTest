from django.db import models

# Create your models here.


class Data(models.Model):
   
   
    ACCNO = models.CharField(max_length=150)
    custstate = models.CharField(max_length=150)
    custpin = models.CharField(max_length=120)
    DPD = models.CharField(max_length=10)
   











