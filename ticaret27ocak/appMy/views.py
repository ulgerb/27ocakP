from django.shortcuts import render, get_object_or_404
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

def ShopDetail(request,slug):
    product = get_object_or_404(ProductStok, product__slug = slug)
    
    listprice = []
    listcolor = []
    listsize = []
    sizeprice = product.sizeletter.all()
    for i in range(len(sizeprice)):
        listprice.append(sizeprice[i].price)
        listcolor.append(sizeprice[i].color.styletitle)
        listsize.append(sizeprice[i].size.slug)
    
    print(listprice)
    print(listcolor)
    print(listsize)
    print("============================")
    if listcolor[0] == "black" and listsize[0] == "m":
        print(listprice[0])
    
    context = {
        "product":product,
    }
    return render(request,'shop-single.html',context)