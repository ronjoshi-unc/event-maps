from django.db import models
from datetime import date
import geocoder
from django.contrib.auth.models import User

# Create your models here.

class InterestTag(models.Model):
    name = models.CharField(max_length=100, default="")

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    birthday = models.DateField()
    bio = models.CharField(max_length=140, default="")

    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_long = models.DecimalField(max_digits=9, decimal_places=6)

    tags = models.ManyToManyField(InterestTag)

    avatar = models.ImageField(upload_to='avatars', default='default_profile_picture.png')

class Event(models.Model):
    title = models.CharField(max_length = 100, default="")
    time = models.DateField()
    all_day = models.BooleanField(default=False)
    location_name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length = 1500)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_long = models.DecimalField(max_digits=9, decimal_places=6)
    tags = models.ManyToManyField(InterestTag)
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    users_managing = models.ManyToManyField(CustomUser, related_name="+")
    users_attending = models.ManyToManyField(CustomUser, related_name="+")

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
