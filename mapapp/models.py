from django.db import models

# Create your models here.
class location(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    address = models.TextField()
    description = models.TextField()
    class Meta:
        db_table='location'