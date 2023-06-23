# email_sender/views.py

from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
import json









template = 'tracking'
subject = 'Order Tracking Update'









def send_emails(request):
    with open('email_list.json') as f:
        data = json.load(f)

    emails = data['emails']
    success_messages = []
    error_messages = []

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

            success_messages.append(f"Email sent successfully to {email}")
        except:
            error_messages.append(f"Failed to send email to {email}")

    return render(request, 'email_sender/sent_emails.html', {
        'success_messages': success_messages,
        'error_messages': error_messages,
    })
