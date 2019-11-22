from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import login, authenticate
from Djwitter.twitterusers.forms import SignUpForm
from django.contrib.auth.models import User
from Djwitter.twitterusers.models import TwitterUser
from django.contrib.auth.decorators import login_required


def signup(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            TwitterUser.objects.create(
                user=user
            )
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, html, {'form': form})

@login_required
def follow(request, username):
    current_twitter_user = request.user.twitteruser
    target_user = User.objects.get(username=username)
    target_twitter_user = TwitterUser.objects.get(user=target_user)

    current_twitter_user.follows.add(target_twitter_user)

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def unfollow(request, username):
    current_twitter_user = request.user.twitteruser
    target_user = User.objects.get(username=username)
    target_twitter_user = TwitterUser.objects.get(user=target_user)

    current_twitter_user.follows.remove(target_twitter_user)

    return redirect(request.META.get('HTTP_REFERER', '/'))