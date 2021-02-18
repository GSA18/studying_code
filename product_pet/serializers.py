from rest_framework import serializers
from .models import ProductPet, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProdutoPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPet
        fields = '__all__'
