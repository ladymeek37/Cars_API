from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.Model_serializer):
    class Meta:
        model = Car()
        fields = ['id', 'make', 'model', 'year', 'price']