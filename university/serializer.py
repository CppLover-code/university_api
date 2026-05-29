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