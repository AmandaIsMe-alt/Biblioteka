from rest_framework import serializers
from Books.models import Follow
from Copies.models import Copy
from Copies.models import Borrow
from datetime import timedelta, datetime
import ipdb


class CopySerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj: Copy) -> dict:
        all_copies = Copy.objects.all()
        count_total_amount = all_copies.filter(book_id=obj.book_id)
        return count_total_amount.count()

    class Meta:
        model = Copy
        fields = ["id", "total_amount", "borrow_amount", "book_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)

    # def get_borrow_amount(self, obj: Copy) -> dict:


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ["id", "borrow_date", "return_date", "returned"]
        read_only_fields = ["return_date", "id"]

    def create(self, validated_data):
        copy = Copy.objects.filter(id=validated_data["copy_id"]).first()

        followers = Follow.objects.filter(book=copy.id).count()

        date_now = datetime.now() + timedelta(days=5)

        if followers > 10:
            date_now += timedelta(days=3)
        elif followers > 5:
            date_now += timedelta(days=5)
        else:
            date_now += timedelta(days=7)

        while date_now.isoweekday() == 6 or date_now.isoweekday() == 7:
            date_now += timedelta(days=1)

        validated_data["return_date"] = date_now

        return Borrow.objects.create(**validated_data)
