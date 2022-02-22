from rest_framework import serializers
from .models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['first_name','last_name','email','phone_number','category','Shop_name','commodities','location']