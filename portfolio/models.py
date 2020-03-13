from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    first_name      = models.CharField(max_length=1000)
    last_name       = models.CharField(max_length=1000)
    email           = models.CharField(max_length=1000)

class Tweets(models.Model):
    id             = models.BigIntegerField(primary_key=True)
    tweetText      = models.CharField(max_length=1000, default='NA', null=True)
    user           = models.CharField(max_length=1000, default='NA', null=True)
    followers      = models.IntegerField(default='NA', null=True)
    date           = models.DateTimeField(max_length=200, default=timezone.now, null=True)
    location       = models.CharField(max_length=1000, default='NA', null=True)
    coordinates_lat= models.CharField(max_length=1000, default='NA', null=True)
    coordinates_lon= models.CharField(max_length=1000, default='NA', null=True)

class TweetsCount(models.Model):
    count          = models.IntegerField(default='NA', null=True)
    date           = models.DateTimeField(null=True, default='2012-09-04 06:00:00')
