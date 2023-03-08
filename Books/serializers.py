from rest_framework import serializers
from .models import Book, Follow


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","title","genre","author","release_year",]

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "user", "book"]
        read_only_fields = ["id", "user", "book"]


    def create(self, validated_data):
        return super().create(validated_data)
    
class AlreadyFollowError(Exception):
    def __init__(self, message):
        self.message = message