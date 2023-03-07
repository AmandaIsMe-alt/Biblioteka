from rest_framework import serializers
from Books.serializers import BookSerializer
from Copies.models import Copy

class CopySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book = BookSerializer()
    total_amount =  serializers.DateTimeField(auto_now_add=True)
    borrow_amount =  serializers.DateTimeField(auto_now_add=True)