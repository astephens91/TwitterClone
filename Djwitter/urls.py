"""Djwitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Djwitter import views
from Djwitter.authentication.urls import urlpatterns as auth_urls
from Djwitter.twitterusers.urls import urlpatterns as users_urls
from Djwitter.notifications.urls import urlpatterns as notif_urls
from Djwitter.tweets.urls import urlpatterns as tweet_urls
from Djwitter.tweets.models import Tweet
from Djwitter.twitterusers.models import TwitterUser
from Djwitter.notifications.models import Notifications

admin.site.register(Tweet)
admin.site.register(TwitterUser)
admin.site.register(Notifications)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('tweet/<int:id>/', views.tweetview, name='specifictweet'),
    path('userprofile/<int:id>/', views.profileview, name='profile')
    
]

urlpatterns += auth_urls
urlpatterns += tweet_urls
urlpatterns += users_urls
urlpatterns += notif_urls
