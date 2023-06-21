# email_sender/urls.py

from django.urls import path
from email_sender import views

app_name = 'email_sender'
urlpatterns = [
    path('send-emails/', views.send_emails, name='send_emails'),
]
