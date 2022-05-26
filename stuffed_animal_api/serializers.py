from rest_framework import serializers
from .models import StuffedAnimal


class StuffedAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "name", "manufacturer", "description", "created_on")
        model = StuffedAnimal
