# email_sender/views.py

from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
import json
from email_sender_project.settings import EMAIL_HOST_USER
from datetime import date









template = 'promotion_mens_oversized'
subject = "🎉 Discover Stylish Comfort: Women's Oversized T-Shirts at BaroMondo + Get 10% Off with Code GET10INSTANT! 🎉"









def send_emails(request):
    with open('email_list.json') as f:
        data = json.load(f)

    emails = data['emails']
    success_messages = []
    error_messages = []
    template_to_show = template + ".html"
    sending_email = EMAIL_HOST_USER
    subject_to_show = subject
    today_date = date.today()
    today = today_date.strftime("%B %d, %Y")
    
 

    for email in emails:
       
        try:
            # Render the custom email template
            email_body = render_to_string('email_sender/' + template + '.html')

            # Create an EmailMessage object
            email_message = EmailMessage(
                subject=subject,
                body=email_body,
                from_email='your-email@example.com',  # Set the 'from' email address
                to=[email],
            )
            email_message.content_subtype = "html"  # Set the content type as HTML

            
          

            # Send the email
            email_message.send()

            
            print(f"Email sent successfully to {email}")

            success_messages.append(f"Email sent successfully to {email}")
        except:
           
            error_messages.append(f"Failed to send email to {email}")
            print(f"Failed to send email to {email}")

    success_messages_count = len(success_messages)
   

    error_messages_count = len(error_messages)
   

    return render(request, 'email_sender/sent_emails.html', {
        'success_messages': success_messages,
        'error_messages': error_messages,
        'template_to_show' : template_to_show,
        'sending_email' : sending_email,
        'subject_to_show' : subject_to_show,
        'today' : today,
        'success_messages_count' : success_messages_count,
        'error_messages_count' : error_messages_count
        
    })
