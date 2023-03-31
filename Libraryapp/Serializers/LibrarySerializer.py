from rest_framework import serializers
from Libraryapp.models import Library


class LibraryLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = (
            "email",
            "password",
        )

class LibraryRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = (
            "name",
            "address",
            "email",
            "password",
        )

class LibraryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = (
            "id"
        )