from django.db import models

# Create your models here.
class Airports(models.Model):
    airportname=models.CharField(max_length=30)
    destinyname=models.CharField(max_length=30)
    arrivaltime=models.DateTimeField()
    departtime=models.DateTimeField()
    def __str__(self):
        return (self.airportname)
    
