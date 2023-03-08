from rest_framework import serializers
from Books.serializers import BookSerializer
from Copies.models import Copy
from Users.serializers import UserSerializer


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "teste", "total_amount", "borrow_amount"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)

