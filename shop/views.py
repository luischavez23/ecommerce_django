from django.shortcuts import render

from .models import Product, Category

def index(request):
    categoryList = Category.objects.all()
    productList = Product.objects.all()
    
    context ={
        "products":productList,
        "categories":categoryList
    }
    
    return  render(request, 'index.html', context)