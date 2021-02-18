from rest_framework import viewsets
from .serializers import CategorySerializer, ProdutoPetSerializer
from .models import Category, ProductPet


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class ProductPetViewset(viewsets.ModelViewSet):
    queryset = ProductPet.objects.all().order_by('name')
    serializer_class = ProdutoPetSerializer
