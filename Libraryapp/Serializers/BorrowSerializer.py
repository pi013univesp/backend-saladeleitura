from rest_framework import serializers
from Libraryapp.models import Borrow

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = (
            "id",
            "book_fk",
            "client_fk",
            "library_fk",
            "borrow_date",
            "end_date"
        )

class GETBorrowSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book_fk.title')
    client_name = serializers.CharField(source='client_fk.name')
    library_name = serializers.CharField(source='library_fk.name')

    class Meta:
        model = Borrow
        fields = (
            "id",
            "book_fk",
            "client_fk",
            "library_fk",
            "borrow_date",
            "end_date",
            "return_date",
            "book_title",
            "client_name",
            "library_name",
        )
