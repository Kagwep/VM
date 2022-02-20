from django.db import models
from Shop.models import Shop

# Create your models here.
class product(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, verbose_name='name of product')
    pcat = (
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
    )

    product_category = models.CharField(max_length=100, verbose_name="product category", choices=pcat)

    subCat = (
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
        ('Electronics','Electronics'),
    )

    product_subcategory = models.CharField(max_length=100,verbose_name='product subcategory', choices=subCat)
    description = models.TextField()
    price = models.CharField(max_length=50, verbose_name='Product price')
    