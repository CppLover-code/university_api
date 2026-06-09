from celery import shared_task

@shared_task
def send_welcome_email(username):

    print(
        f"Welcome email sent to {username}"
    )

    return f"Email sent to {username}"



