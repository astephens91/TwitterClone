from django.shortcuts import render, HttpResponseRedirect, reverse
from Djwitter.notifications.models import Notifications
from Djwitter.twitterusers.models import TwitterUser
from django.contrib.auth.decorators import login_required



@login_required
def notif_view(request, id):

    html = 'notification.html'
    twitteruser = TwitterUser.objects.filter(id=id).first()
    data = Notifications.objects.filter(user=twitteruser)
    for item in data:
        item.delete()
    return render(request, html, {'data': data})
