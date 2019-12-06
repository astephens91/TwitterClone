from django.urls import path
from Djwitter.tweets import views

urlpatterns = [
    path('addtweet/', views.addtweet_view.as_view(), name='addtweet')
]
