from rest_framework import serializers

from .models import (
    Teacher,
    Subject,
    Student
)

# Автоматически создает serializer по модели
class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject     # говорим какую модель сериализируем
        fields = "__all__"  # включить все поля модели

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"