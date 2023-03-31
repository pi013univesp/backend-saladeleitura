from rest_framework import serializers
from Libraryapp.models import Literary_genres


class LiteraryGenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literary_genres
        fields = (
            "id",
            "genre",
        )
