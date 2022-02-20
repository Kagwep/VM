from tkinter import CASCADE
from django.db import models
from Registration.models import AppUser
# Create your models here.
class Shop(models.Model):
    owner = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100,verbose_name='Enter your shops name')
    contact =  models.CharField(max_length=100, verbose_name="Enter your shops contact")
    com = (
       ("Electronics","Electronics") ,
       ("Clothes","Clothes") ,
       ("Food","Food") ,
       ("House to let","House to let") ,
       ("Furniture","Furniture") ,
    )
    commodities = models.CharField(max_length=200, verbose_name="Shop category")
    location = models.CharField(max_length=200, verbose_name='Shops location')
    date_joined = models.DateField(auto_now_add=True)