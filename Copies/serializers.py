from rest_framework import serializers
from Books.models import Follow
from Copies.models import Copy
from Copies.models import Borrow
from datetime import timedelta, datetime
from rest_framework.exceptions import APIException
from rest_framework import status


class CopyExeption(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class CopySerializer(serializers.ModelSerializer):

    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj: Copy) -> dict:
        all_copies = Copy.objects.all()
        count_total_amount = all_copies.filter(book_id=obj.book_id)
        return count_total_amount.count()

    class Meta:
        model = Copy
        fields = ["id", "total_amount", "is_active", "book_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)

    # def get_borrow_amount(self, obj: Copy) -> dict:


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ["id", "user", "copy", "borrow_date", "return_date", "returned"]
        read_only_fields = ["user", "copy", "return_date", "id"]

    def create(self, validated_data):

        copies = Copy.objects.all()

        copy_filter = copies.filter(id=validated_data["copy_id"]).first()

        if not copy_filter:
            raise CopyExeption("Copy does not exist")
        elif copy_filter.is_active is False:
            raise CopyExeption("Copy is already in use")

        copy_filter.is_active = False
        copy_filter.save()

        followers = Follow.objects.filter(book=copy_filter.book_id).count()

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
