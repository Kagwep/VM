from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import AppUser
from .serializers import AppUserSerializer
class AppUserViewset(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer