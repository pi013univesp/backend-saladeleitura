from rest_framework import serializers
from Libraryapp.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "literary_genre_fk",
            "publisher",
            "number_of_pages",
            "resume",
        )

class GETBookSerializer(serializers.ModelSerializer):
    literary_genre_name = serializers.CharField(source='literary_genre_fk.genre')

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "literary_genre_fk",
            "publisher",
            "number_of_pages",
            "resume",
            "literary_genre_name",
        )