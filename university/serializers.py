rom users.models import User
from rest_framework import serializers

from .models import Student


class StudentRegistrationSerializer(
    serializers.Serializer
):

    username = serializers.CharField()
    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )

    subjects = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )

    def create(self, validated_data):

        subjects = validated_data.pop(
            "subjects",
            []
        )

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role="student",
        )

        student = Student.objects.create(
            user=user
        )

        student.subjects.set(subjects)

        return student