from django.db import models
from users.models import User

class Teacher(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_profile"
    )

    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    

class Subject(models.Model):

    title = models.CharField(max_length=100)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    def __str__(self):
        return self.title
    

class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    subjects = models.ManyToManyField(
        Subject,
        related_name="students"
    )

    def __str__(self):
        return self.user.username
    


    # РАЗОБРАТЬ КОД!!!!!!!!!!!!!!!