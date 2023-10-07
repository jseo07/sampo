from django.db import models

# Create your models here.
class location(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    address = models.TextField()
    description = models.TextField()
    
    def to_json(self):
        return{
            "x":self.x,
            "y":self.y,
            "address":self.address,
            "description":self.description
        }
    
    class Meta:
        db_table='location'