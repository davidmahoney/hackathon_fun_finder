#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    

class Event(models.Model):
    owner_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    location = models.PointField()
    address = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    url = models.URLField()
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category)
    objects = models.GeoManager()

    def __str__(self):
        return self.name
