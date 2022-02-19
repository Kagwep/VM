from django.db import models

# Create your models here.
class shop(models.Model):
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
    