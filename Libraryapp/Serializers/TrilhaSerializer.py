from rest_framework import serializers
from Libraryapp.models import Trilha, TrilhaLivros

class TrilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilha
        fields = (
            "id",
            "name"
        )

class TrilhaLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrilhaLivros
        fields = (
            "id",
            "library_fk",
            "book_fk",
            "trilha_fk",
            "posicao_na_trilha"
        )

class GETTrilhaLivroSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book_fk.title')
    book_author = serializers.CharField(source='book_fk.author')
    book_publisher = serializers.CharField(source='book_fk.publisher')
    trilha_name = serializers.CharField(source='trilha_fk.name')

    class Meta:
        model = TrilhaLivros
        fields = (
            "id",
            "library_fk",
            "book_fk",
            "trilha_fk",
            "book_title",
            "posicao_na_trilha",
            "book_author",
            "book_publisher",
            "trilha_name"
        )