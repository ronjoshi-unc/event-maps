from django.db import models
from django.contrib.auth.models import User
#from notifications.base.models import AbstractNotification
from datetime import date
#from taggit.managers import TaggableManager
import geocoder

# Create your models here.
mapbox_access_token = 'pk.eyJ1Ijoia21nb3ZpbmQiLCJhIjoiY2ttaHZ2c2k1MGJkaDJ3cW90dzhzcDl3ZyJ9.8gnW35BhS9WSZaCBTOJ1IQ'

class InterestTag(models.Model):
    name = models.CharField(max_length=100, default="")

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(default="")
    location_lat = models.FloatField(blank=True, null=True)
    location_long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.location_lat = g[0]
        self.location_long = g[1]
        return super(CustomUser, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)

class Event(models.Model):
    title = models.CharField(max_length = 100, default="")
    time = models.DateField()
    location_name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length = 1500)
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    address = models.TextField(default="")
    location_lat = models.FloatField(blank=True, null=True)
    location_long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.location_lat = g[0]
        self.location_long = g[1]
        return super(Event, self).save(*args, **kwargs)
