from rest_framework import serializers
from Books.serializers import BookSerializer
from Copies.models import Copy
from Users.serializers import UserSerializer

class CopySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book = BookSerializer()
    total_amount =  serializers.IntegerField()
    borrow_amount =  serializers.IntegerField()

class BorrowSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    borrow_date = serializers.DateTimeField(auto_now_add=True)
    return_date = serializers.DateTimeField(auto_now_add=True)
    user = UserSerializer()
    copy = CopySerializer()