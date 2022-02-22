from django.shortcuts import render

# Create your views here.
from .models import product
from rest_framework  import viewsets
from .serializers import productSerualizer


class ProductViewset(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerualizer
    