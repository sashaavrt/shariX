from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_notify_mail(subject: str, message_template: str, recipient_list: list, context: dict):
    try:
        html_message = render_to_string(message_template, context)
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            html_message=html_message
        )
    except Exception as e:
        print(f"Error when sending an e-mail: {e}")
