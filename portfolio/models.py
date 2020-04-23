from django.db import models
from django.utils import timezone

class Tweets(models.Model):
    id             = models.BigIntegerField(primary_key=True)
    tweetId        = models.CharField(max_length=1000, default='NA', null=True)
    username       = models.CharField(max_length=1000, default='NA', null=True)
    videoImage     = models.CharField(max_length=1000, default='NA', null=True)
