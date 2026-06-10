from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email, full_name, username):

    send_mail(
        subject="Welcome to University API",
        message = f"""
            Hello, {full_name}!

            Your account has been successfully created in the University API system.

            Username: {username}

            We are glad to welcome you to our educational platform.

            We wish you success in your studies and a great learning experience!

            Best regards,
            University API Team
            """,
        from_email=None,
        recipient_list=[email],
        fail_silently=False,
    )

    return f"Email sent to {full_name}"



