from django.urls import path
from Djwitter.twitterusers import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<str:username>/follow', views.follow, name='follow'),
    path('<str:username>/unfollow', views.unfollow, name='unfollow')
]