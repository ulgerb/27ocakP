from django.shortcuts import render
from .models import *

def index(request):
    context = {}
    return render(request,'index.html',context)

def About(request):
    context = {}
    return render(request,'about.html',context)

def Contact(request):
    context = {}
    return render(request,'contact.html',context)

def Shop(request):
    products = ProductStok.objects.all()
    for i in products:
        print(i.sizeletter.first())
        for j in i.sizeletter.all():
            print(j)
    context = {
        "products":products,
    }
    return render(request,'shop.html',context)

def ShopDetail(request):
    context = {}
    return render(request,'shop-single.html',context)