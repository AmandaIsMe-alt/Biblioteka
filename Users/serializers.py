from rest_framework import serializers
from .models import User
from Copies.models import Borrow
from Copies.serializers import BorrowSerializer


class UserSerializer(serializers.ModelSerializer):
    user_borrows = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id","username","email","password","is_librarian","blocked_until","is_active", "is_superuser", "user_borrows"]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}
        depth = 1

    def get_user_borrows(self, obj):
        borrows = Borrow.objects.filter(user_id=obj.id)
        serializer = BorrowSerializer(borrows, many=True)
        return serializer.data

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
