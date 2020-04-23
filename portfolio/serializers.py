from django.contrib.auth.models import User
from rest_framework import serializers
from portfolio.models import Tweets

class TweetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweets
        fields = ('id', 'tweetId', 'username', 'videoImage')
