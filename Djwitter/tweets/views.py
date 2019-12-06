from django.shortcuts import render, HttpResponseRedirect, reverse
from Djwitter.tweets.models import Tweet
from Djwitter.tweets.forms import AddTweet
from Djwitter.notifications.models import Notifications
from Djwitter.twitterusers.models import TwitterUser
from django.views import View
import re



class addtweet_view(View):
    form_class = AddTweet
    initial = {'key':'value'}
    html = 'generic_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.html, {'form': form})
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
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
        return render(request, self.html, {'form': form})
