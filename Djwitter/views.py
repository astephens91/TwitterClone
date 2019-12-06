from django.shortcuts import render, HttpResponseRedirect, reverse
from Djwitter.tweets.models import Tweet
from django.contrib.auth.decorators import login_required
from Djwitter.notifications.models import Notifications
from Djwitter.twitterusers.models import TwitterUser
from django.views import View


class index(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:
            html = "index.html"

            notif = Notifications.objects.filter(user=request.user.twitteruser).count()

            following_list  = request.user.twitteruser.follows.all()
            user_tweets = Tweet.objects.filter(created_by=request.user.twitteruser) 
            following_tweets = Tweet.objects.filter(created_by__in=following_list)
            tweets = user_tweets | following_tweets

            return render(request, html, {'tweets': tweets, 'notifications': notif})


class tweetview(View):
    def get(self, request, id):
        html = "specifictweet.html"

        tweet = Tweet.objects.filter(id=id)

        return render(request, html, {'tweet': tweet})


class profileview(View):
    def get(self, request, id):
        html = "userprofile.html"


        user = TwitterUser.objects.filter(id=id)
        
        user_tweets = Tweet.objects.filter(created_by=id)

        tweet_count = user_tweets.count()

        return render(request, html, {'tweets': user_tweets, 'user': user, 'tweet_count': tweet_count})