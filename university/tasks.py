from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email, username, full_name):

    send_mail(
        subject="Добро пожаловать!",
        message=(
            f"Здравствуйте, {full_name}!\n\n"
            "Вы успешно зарегистрированы "
            "в системе University API.\n\n"
            "Желаем успехов в обучении!"
        ),
        from_email=None,
        recipient_list=[email],
        fail_silently=False,
    )

    return f"Email sent to {username} - {full_name}"



