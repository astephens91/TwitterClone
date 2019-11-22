from django import forms
from Djwitter.tweets.models import Tweet


class AddTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'content'
        ]