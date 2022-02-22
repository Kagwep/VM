from django.shortcuts import render
from itsdangerous import Serializer
from .models import Shop
from rest_framework import viewsets
from .serializers import shopSerializer

# Create your views here.
class shopViewset(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = shopSerializer