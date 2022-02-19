from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)