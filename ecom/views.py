from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class LatestProductList(APIView):
    def get_queryset(self):
        products = Product.objects.all()
        return products

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_data = request.data

        new_product = Product.objects.create(
            reference=product_data["reference"],
            name=product_data["name"],
            image=product_data["image"],
            description=product_data["description"]
        )

        new_product.save()

        serializer = ProductSerializer(new_product)
        serializer.is_valid()

        return Response(serializer.data)

