from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from .tasks import send_welcome_email

@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):

    if created:

        full_name = (
            f"{instance.user.first_name} "
            f"{instance.user.last_name}"
        )
        username = instance.user.username

        send_welcome_email.delay(
            instance.user.email,
            full_name,
            username
        )