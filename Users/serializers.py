from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password","is_librarian","is_blocked","is_active", "is_superuser"]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        if validated_data['is_librarian']:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)
    

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data["password"])

        instance.save()

        return instance
