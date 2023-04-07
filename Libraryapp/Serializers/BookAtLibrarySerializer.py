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
    book_title = serializers.CharField(source='book_fk.title')
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
        )