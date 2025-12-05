from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('send-emails/', views.send_emails, name='send_emails'),
]