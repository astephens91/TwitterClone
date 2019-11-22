from django.urls import path
from Djwitter.notifications import views

urlpatterns = [
    path('notification/<int:id>/', views.notif_view, name='notifications')
]