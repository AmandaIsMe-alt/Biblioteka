from rest_framework import serializers
from Books.models import Follow
from Copies.models import Copy
from Copies.models import Borrow
from datetime import timedelta, datetime


class CopySerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()
    
    class Meta:
        model = Copy
        fields = ["id", "total_amount", "borrow_amount", "book_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)

    def get_total_amount(self, obj: Copy) -> dict:
        all_copies = Copy.objects.all()
        count_total_amount = all_copies.filter(book_id=obj.book_id)
        return count_total_amount.count()
    
    # def get_borrow_amount(self, obj: Copy) -> dict:


class BorrowSerializer(serializers.ModelSerializer):
    return_date = serializers.SerializerMethodField()

    def create(self, validated_data):
        return Borrow.objects.create(**validated_data)
    
    
    
    class Meta:
        model = Borrow
        fields = ["id", "borrow_date", "return_date", "returned"]
        read_only_fields = ["return_date", "id"]

    