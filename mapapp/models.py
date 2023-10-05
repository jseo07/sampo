from django.db import models

# Create your models here.
class Locations(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    address = models.TextField()
    description = models.TextField()