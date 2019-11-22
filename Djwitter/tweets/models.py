from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Djwitter.twitterusers.models import TwitterUser 


class Tweet(models.Model):
    content = models.CharField(max_length=280)
    post_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(TwitterUser, on_delete=models.DO_NOTHING, related_name='created_by+')

    # this allows us to display the tweets in order of newest post first
    class Meta:
        ordering = ('-post_date', )

    def __str__(self):
        return "{0} at {1}: {2}...".format(self.created_by,
                                           self.post_date,
                                           self.content[:20])
