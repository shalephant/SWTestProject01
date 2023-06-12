from django.db import models

# Create your models here.
class Car(models.Model):
    maker = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
    year = models.IntegerField()
    doors = models.IntegerField(default=4)