from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages

# Create your views here.
from category.models import *
from.models import *
def Subcatdemo(req):
    all_data=Categories.objects.all()
    all_subcat = SubCategories.objects.select_related('cat_id').all()
    data={'cats':all_data,'subcat':all_subcat}
    return render(req,'subcat/subcat.html',data)#'subcategory/subcat.html'

def SubcatInsert(req):
    cat_id=req.POST.get('cat_name')
    cat_Name=req.POST.get('sub_cat_name')
    category_instance=get_object_or_404(Categories,id=cat_id)
    sub_cat_obj=SubCategories()
    sub_cat_obj.Name=cat_Name
    sub_cat_obj.cat_id=category_instance
    sub_cat_obj.save()

    messages.success(req, "sub Category create successfully")

    return redirect('SubcatePageShow')