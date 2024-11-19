from django.db import models
from category.models import *
from subcat.models import *
# Create your models here.
class Product(models.Model):
    Tittle=models.CharField(max_length=100,unique=True)
    Description=models.CharField(max_length=100,unique=True)
    Actual_price= models.DecimalField(max_digits=10, decimal_places=2)
    Discount= models.DecimalField(max_digits=3, decimal_places=2)
    Image=models.ImageField(upload_to='myimages/')
    sub_cat_id=models.ForeignKey(SubCategories,related_name='products',on_delete=models.CASCADE)