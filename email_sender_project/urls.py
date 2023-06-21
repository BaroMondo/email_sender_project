# email_sender_project/urls.py

from django.contrib import admin
from django.urls import path, include
from email_sender import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.send_emails, name='send_emails'),  # Add this line
    path('email-sender/', include('email_sender.urls')),
]



