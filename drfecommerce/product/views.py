
from rest_framework import viewsets

from product.models import Brand, Category, Product
from product.serializers import (BrandSerializer, CategorySerializer,
                                 ListProductSerializer, ProductSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):

        if self.request.method == "GET":
            return ListProductSerializer
        return ProductSerializer
