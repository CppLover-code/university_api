from django.db import models
from django.contrib.auth.models import AbstractUser

"""
django уже имеет встроенную модель пользователя.
Стандартный User содержит:
username
password
email
first_name
last_name

Использую AbstractUser, чтоб сохранить весь функционал django,
добавить свои поля, чтоб расширить стандартного пользователя.
"""

class User(AbstractUser):

    # Набор допустимых ролей
    # в базе хранится teacher, а в админке отображается Teacher
    ROLE_CHOICES = (
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("admin", "Admin"),
    )

    role = models.CharField(
        max_length=20,
        choices= ROLE_CHOICES,
        default="student"
    )

    def __str__(self):
        return self.username
    
