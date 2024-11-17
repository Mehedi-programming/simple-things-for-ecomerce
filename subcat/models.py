from django.db import models

from category.models import *
# Create your models here.
class SubCategories(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    cat_id=models.ForeignKey(Categories,related_name='Subcategories',on_delete=models.CASCADE)