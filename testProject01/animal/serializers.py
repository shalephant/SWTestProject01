from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.Serializer):
    class Meta:
        model = Animal
        fileds = "__all__"