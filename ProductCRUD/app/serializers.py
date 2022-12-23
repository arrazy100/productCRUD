from rest_framework import serializers

from .models import (
    CategoryModel,
    ProductModel
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True, source='get_products')

    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'products')