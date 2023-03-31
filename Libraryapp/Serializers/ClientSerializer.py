from rest_framework import serializers
from Libraryapp.models import Client

class ClientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "name",
            "phone",
            "address",
        )

class ClientGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "name",
            "phone",
            "address",
        )