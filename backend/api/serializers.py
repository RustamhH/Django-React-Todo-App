from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
from django.core.validators import RegexValidator



class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$",
                message="Password must be at least 8 characters long and include 1 uppercase letter , 1 lowercase letter and a special char.",
            )
        ]
    )

    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}