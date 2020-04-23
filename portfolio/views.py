from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from portfolio.models import Tweets
from portfolio.serializers import TweetsSerializer
from rest_framework import viewsets, status, serializers
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
import psycopg2
import os
import pusher
import preprocessor as p
import requests
import time
from datetime import datetime as dt
from pprint import pprint
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
import tweepy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

consumer_key = 'oTEY24ghsRqntYvkhQtajGBVX'
consumer_secret = 'RzXg2wJABf8JYSMrgUhFL6GMSKxYTJNYTKQVoHJEya0heRPJ2s'
access_token = '393160291-SMzRKhJildn4UaGbGq4WwXqq71iTweUkBIXes2bU'
access_token_secret = 'dfXmz7ReWJKBmSU5rWmUu3DbQqvygpzcTHU9Z4L86LmXg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    # When data is received
    def on_data(self, data):

        # # Error handling
        try:

         # Make it JSON
            tweet = json.loads(data)
            # pprint(tweet)


            if not tweet['retweeted'] and 'RT @' not in tweet['text']:
              if tweet['extended_entities'] != None:
                video_image = tweet['extended_entities']['media'][0]['media_url']
                pprint(tweet['extended_entities']['media'][0]['video_info']['variants'][1]['url'])
                video_url = tweet['extended_entities']['media'][0]['video_info']['variants'][1]['url']
              # Get user via Tweepy so we can get their number of followers
                twitter_name = tweet['user']['screen_name']

                try:
                    text = tweet.extended_tweet['full_text']
                
                except AttributeError:
                    text = tweet['text']

                if '.mp4' in video_url:
                    # assign all data to Tweet object
                    tweet_data = Tweet(
                        video_url,
                        twitter_name,
                        video_image
                    )

                    # Insert that data into the DB
                    tweet_data.insertTweet()

                    tweet_count = Tweets.objects.count()
                    time = str(dt.now())
                    print(time)
                    print(tweet_count)

                    current_count = TweetCount(
                        tweet_count,
                        time
                    )

                    current_count.insertTweetCount()  


            else:
                pass


        #Let me know if something bad happens
        except Exception as e:
            print(e)
            pass

        return True

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode='extended')

myStream.filter(
  track=['zachalexander'],
  languages= ['en'],
  is_async=True
)

pusher_client = pusher.Pusher(
  app_id='978095',
  key='c370de797b5f03b744ff',
  secret='edfd30117dc6f4650a18',
  cluster='us2',
  ssl=True
)

# Twitter Streaming API credentials

consumer_key = 'oTEY24ghsRqntYvkhQtajGBVX'
consumer_secret = 'RzXg2wJABf8JYSMrgUhFL6GMSKxYTJNYTKQVoHJEya0heRPJ2s'
access_token = '393160291-SMzRKhJildn4UaGbGq4WwXqq71iTweUkBIXes2bU'
access_token_secret = 'dfXmz7ReWJKBmSU5rWmUu3DbQqvygpzcTHU9Z4L86LmXg'

# Class for defining the tweet count
class TweetCount():

    # Data on the tweet
    def __init__(self, count, date):
        self.count = count
        self.date = str(date)

        # Inserting that data into the DB
    def insertTweetCount(self):
        #SQlite3 connection
        # conn = sqlite3.connect('users.sqlite3')
        # c = conn.cursor()
        # c.execute("UPDATE portfolio_tweetscount SET count=%s, date=%r WHERE (SELECT count FROM portfolio_tweetscount ORDER BY count LIMIT 1)" %
        #     (self.count, self.date))
        # conn.commit()

        # Postgres connection
        DATABASE_URL = os.environ['DATABASE_URL']
        connpsy = psycopg2.connect(DATABASE_URL, sslmode='require')
        cpsy = connpsy.cursor()
        sql = """UPDATE portfolio_tweetscount SET "count"=%s, "date"=%s WHERE id = NULL"""
        cpsy.execute(sql, (self.count, self.date))
        pusher_client.trigger('my-channel', 'tweetcount', {
            'number': self.count,
            'date': str(self.date)
        })
        connpsy.commit()

# Class for defining a Tweet
class Tweet():

    # Data on the tweet
    def __init__(self, tweetId, username, videoImage):
        self.tweetId = tweetId
        self.username = username
        self.videoImage = videoImage

    # Inserting that data into the DB
    def insertTweet(self):
        #SQLite3 connection
        # conn = sqlite3.connect('users.sqlite3')
        # c = conn.cursor()
        # c.execute("INSERT INTO portfolio_tweets (tweetId, username, videoImage) VALUES (?, ?, ?)",
        #     (self.tweetId, self.username, self.videoImage))
        # conn.commit()

        try:
            # Postgres connection
            DATABASE_URL = os.environ['DATABASE_URL']
            connpsy = psycopg2.connect(DATABASE_URL, sslmode='require')
            # sql = """ INSERT INTO portfolio_tweets (id, tweetText, user, followers, date, location, coordinates_lat, coordinates_lon) VALUES (?, ?, ?, ?, ?, ?, ?, ?) """
            cpsy = connpsy.cursor()
            cpsy.execute("""INSERT INTO portfolio_tweets("tweetId", "username", "videoImage") VALUES (%s, %s, %s);""", 
                (self.tweetId, self.username, self.videoImage))
            pusher_client.trigger('my-channel', 'videodetails', 1)
            connpsy.commit()

        except(Exception, psycopg2.Error) as error:
            if(connpsy):
                print("Failed to insert record", error)
        
        finally:
            if(connpsy):
                cpsy.close()
                connpsy.close()
                print("Connection is closed")

def index(request):
    return HttpResponse("<h1>Hello, Zach</h1>")

class TweetsViewSet(viewsets.ModelViewSet):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer

class TweetListView(ListView):
    model = Tweets
    paginate_by = 8

# APIs

@csrf_exempt
def tweet_list_all(request):
    # Get all
    if request.method == 'GET':
        tweets = Tweets.objects.order_by('-id')
        tweets_serializer = TweetsSerializer(tweets, many=True)
        return JsonResponse(tweets_serializer.data, safe=False)

@csrf_exempt
def tweet_list_pagination(request):
    # Get all
    if request.method == 'GET':
        tweets = Tweets.objects.order_by('-id')
        paginator = Paginator(tweets, 16)
        page = request.GET.get('page')
        
        try: 
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        tweets_serializer = TweetsSerializer(posts, many=True)
        return JsonResponse(tweets_serializer.data, safe=False)
 


 