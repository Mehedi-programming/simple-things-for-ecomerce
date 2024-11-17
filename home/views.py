from django.shortcuts import render
from category.models import *
from subcat.models import *
from django.db.models import Prefetch
# Create your views here.
def homePage(req):
    all_data_subcat=SubCategories.objects.prefetch_related('cat_id').all()
    '''for i in all_data_subcat:
        print(i)'''
    categories = Categories.objects.prefetch_related(
        Prefetch('Subcategories', queryset=SubCategories.objects.all())
    ).distinct()
    for category in categories:
        print(f"Category:{category.catName}")
        for subcat in category.Subcategories.all():
            print(f" Subcategory: {subcat.Name}")


    data={'cats_subcat':all_data_subcat}
    return render(req,'home/home.html',data)




