from rest_framework import serializers
from .models import Book, Follow
from Copies.models import Copy
from Genres.serializers import GenreSerializers
from Genres.models import Genre


class BookSerializer(serializers.ModelSerializer):

    genres = GenreSerializers(many=True)
    number_copies_available = serializers.SerializerMethodField()

    def get_number_copies_available(self, obj: Copy) -> dict:
        all_copies = Copy.objects.all()
        count_total_amount = all_copies.filter(book_id=obj.id, is_active=True)
        return count_total_amount.count()

    def create(self, validated_data):
        genres_to_add = validated_data.pop("genres")

        create_book = Book.objects.create(**validated_data)
        for genre in genres_to_add:
            genre_obj = Genre.objects.filter(name__iexact=genre["name"]).first()
            if not genre_obj:
                genre_obj = Genre.objects.create(**genre)
            create_book.genres.add(genre_obj)

        return create_book

    def update(self, instance: Book, validated_data):

        genres_to_update = validated_data.pop("genres")

        if genres_to_update:
            instance.genres.clear()
            for genre in genres_to_update:
                genre_obj = Genre.objects.filter(name__iexact=genre["name"]).first()
                if not genre_obj:
                    genre_obj = Genre.objects.create(**genre)
                instance.genres.add(genre_obj)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        return instance

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "number_copies_available",
            "release_year",
            "publisher_company",
            "synopsis",
            "genres",
        ]
        read_only_fields = ["id", "number_copies_available"]


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
