import email
from unicodedata import category
from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(verbose_name='enter first name', null=False, max_length=100)
    last_name = models.CharField(verbose_name='enter last name', null=False, max_length=100)
    email = models.EmailField(verbose_name='enter last name', null= False)
    phone_number =  models.CharField(verbose_name='enter valid phone number', null=False, max_length=20)
    cat= (
        ('Buyer','Buyer'),
        ('Seller','Seller'),
    )
    category = models.CharField(verbose_name='sing up as ', max_length=20)
    

    #fileds to sellers
    Shop_name = models.CharField(max_length=200, verbose_name= 'enter shop name')
    com = (
       ("Electronics","Electronics") ,
       ("Clothes","Clothes") ,
       ("Food","Food") ,
       ("House to let","House to let") ,
       ("Furniture","Furniture") ,
    )
    commodities = models.CharField(max_length=200, verbose_name="Shop category")
    location = models.CharField(max_length=200, verbose_name='Shops location')

