from rest_framework import serializers
from .models import Variant, Product

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('id', 'specification', 'sku', 'price')


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'reference', 'name', 'image', 'description', 'variants')



