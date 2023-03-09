from rest_framework import serializers
from .models import User
from Copies.serializers import BorrowSerializer


class UserSerializer(serializers.ModelSerializer):
    user_borrow = BorrowSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_librarian",
            "is_blocked",
            "is_active",
            "is_superuser",
            "user_borrow",
        ]
        read_only_fields = ["id", "user_borrow"]
        extra_kwargs = {"password": {"write_only": True}}
        depth = 1

    def create(self, validated_data: dict) -> User:
        if validated_data["is_librarian"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data["password"])

        instance.save()

        return instance
