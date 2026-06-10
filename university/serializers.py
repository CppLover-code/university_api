from users.models import User
from rest_framework import serializers

from .models import Student


class StudentRegistrationSerializer(
    serializers.Serializer
):

    username = serializers.CharField()

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )

    subjects = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )

    def validate(self, attrs):

        if User.objects.filter(
            username=attrs["username"]
        ).exists():

            raise serializers.ValidationError(
                {
                    "username":
                    "Пользователь с таким username уже существует."
                }
            )

        

        return attrs

    def create(self, validated_data):

        subjects = validated_data.pop(
            "subjects",
            []
        )

        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
            role="student",
        )

        student = Student.objects.create(
            user=user
        )

        student.subjects.set(subjects)

        return student
    
    """
    if User.objects.filter(
            email=attrs["email"]
        ).exists():

            raise serializers.ValidationError(
                {
                    "email":
                    "Пользователь с такой почтой уже существует."
                }
            )
    """