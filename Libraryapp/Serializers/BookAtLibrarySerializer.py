from rest_framework import serializers
from Libraryapp.models import Books_at_library

class BookAtLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Books_at_library
        fields = (
            "id",
            "library_fk",
            "book_fk",
            "book_stock",
            "number_of_borrowed_books",
        )


class GETBookAtLibrarySerializer(serializers.ModelSerializer):
    book_id = serializers.CharField(source='book_fk.id')
    book_title = serializers.CharField(source='book_fk.title')
    book_data = serializers.CharField(source='book_fk.data')
    book_especie = serializers.CharField(source='book_fk.especie')
    book_tombo = serializers.CharField(source='book_fk.tombo')
    book_procedencia = serializers.CharField(source='book_fk.procedencia')
    book_author = serializers.CharField(source='book_fk.author')
    book_publisher = serializers.CharField(source='book_fk.publisher')
    library_name = serializers.CharField(source='library_fk.name')

    class Meta:
        model = Books_at_library
        fields = (
            "id",
            "library_fk",
            "book_fk",
            "book_stock",
            "number_of_borrowed_books",
            "book_title",
            "library_name",
            "book_data",
            "book_especie",
            "book_tombo",
            "book_procedencia",
            "book_author",
            "book_publisher",
            "book_id",
        )