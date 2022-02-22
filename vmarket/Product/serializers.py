from rest_framework import serializers
from .models import product

class productSerualizer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'