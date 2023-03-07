from rest_framework import serializers
from .models import Genre


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
