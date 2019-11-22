from django.shortcuts import render, HttpResponseRedirect, reverse
from Djwitter.tweets.models import Tweet
from Djwitter.tweets.forms import AddTweet
from Djwitter.notifications.models import Notifications
from Djwitter.twitterusers.models import TwitterUser
import re


def addtweet_view(request):
    html = 'generic_form.html'

    if request.method == "POST":
        form = AddTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            tweet = Tweet.objects.create(
                content=data['content'],
                created_by=request.user.twitteruser
            )
            if "@" in data['content']:
                tags = re.findall(r"@(\w+)", data['content'])
                for name in tags:
                    tagged_user = TwitterUser.objects.get(user__username=name)
                    Notifications.objects.create(
                        user=tagged_user,
                        tweet=tweet
                    )

        return HttpResponseRedirect(reverse('homepage'))
    form = AddTweet()
    return render(request, html, {'form': form})
