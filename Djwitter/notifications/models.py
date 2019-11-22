from django.db import models
from Djwitter.twitterusers.models import TwitterUser
from Djwitter.tweets.models import Tweet


class Notifications(models.Model):
    user = models.ForeignKey(TwitterUser,
                             on_delete=models.CASCADE,
                             related_name='notification_user'
                             )
    seen = models.BooleanField(default=False)
    
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,)
        
    def __str__(self):
        return f'{self.tweet.content} - {self.tweet.created_by}'

