from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib import messages
from . models import *
 
def catdemo(req):
    return render(req,'category/cat.html')
def catInsert(req):
    cat_Name = req.POST.get('cat_name')
    #validation
    if(('cat_Name')==''):
        #return HttpResponse('category can not have empty')
        messages.error(req, "Your message was sent successfully!")
    elif(len(cat_Name)<5):
        #return HttpResponse('category can not have less than 8 capital')
        messages.error(req, "category can not have less than 8 capital!")
    elif(Categories.objects.filter(catName=cat_Name).exists()):
        #return HttpResponse('this value already exist')
        messages.error(req,"this category already exists ,now you have to entry a new category")
    else:
        # does there have any secondtime valu of cat_Name in the table of catName for class Categories. 
        cat_obj = Categories()
        cat_obj.catName=cat_Name
        cat_obj.save()
        #return HttpResponse(cat_Name)
        messages.success(req, "Category created successfully")

    return redirect('catePageShow')
# Create your views here.
