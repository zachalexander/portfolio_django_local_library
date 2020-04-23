from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    # path('', include(router.urls))
    # url(r'tweets-latest/', views.tweet_list_first),
    url(r'^tweets-all/$', views.tweet_list_pagination),
    url(r'tweets-full/', views.tweet_list_all)
    # url(r'tweet-count/', views.tweetcount_list)
]
