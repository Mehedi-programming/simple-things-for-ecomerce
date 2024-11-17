from django.shortcuts import render
from category.models import *
from subcat.models import *
from django.db.models import Prefetch, Count
# Create your views here.
def homePage(req):
    all_cats_subcats = SubCategories.objects.prefetch_related('cat_id').all()
    '''for i in all_data_subcat:
        print(i)'''
    categories = Categories.objects.annotate(subcat_count=Count('Subcategories')).filter(subcat_count__gt=0).prefetch_related(
        Prefetch('Subcategories', queryset=SubCategories.objects.all())
    ).distinct()
    for category in categories:
        print(f"Category:{category.catName}")
        for subcat in category.Subcategories.all():
            print(f" Subcategory: {subcat.Name}")


    data={'cats_subcat':categories}
    return render(req,'home/home.html',data)




