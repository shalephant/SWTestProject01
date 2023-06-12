from django.db import models

# Create your models here.

class Animal(models.Model):
    family = models.CharField(max_length=50),
    legs = models.IntegerField(default=4),
    can_fly = models.BooleanField(default=False),
    can_swim = models.BooleanField(default=True)