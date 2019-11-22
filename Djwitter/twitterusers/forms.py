from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True,
                                 widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True,
                                widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(
                                    attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(
                                    attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        fields = ['email',
                  'username',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2', ]
        model = User
