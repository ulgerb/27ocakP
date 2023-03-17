from django.shortcuts import render, get_object_or_404, redirect
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
    
    if request.method == "POST":
        submit = request.POST.get("submit")
        if submit == "buy":
            print(request.POST)
            color = request.POST.get("color")
            size = request.POST.get("size")
            count = int(request.POST.get("count"))
            prod = SizeLetter.objects.filter(color__styletitle=color, size__title=size).get()
            price_all = prod.price * count
            shopprod = Shopbasket.objects.filter(product_letter=prod)
            if shopprod.exists(): # filterlanan ürün varsa true
                print(shopprod, price_all)
                shopprod = shopprod.get()
                shopprod.count += count
                shopprod.price_all += price_all
                shopprod.save()
            else:
                shopb = Shopbasket(user = request.user, product_letter = prod,price_all=price_all, count=count )
                shopb.save()
            
            return redirect('/ShopDetail/'+ slug + '/')
            
    
    listprice = []
    listcolor = []
    listsize = []
    sizeprice = product.sizeletter.all()
    for i in range(len(sizeprice)):
        listprice.append(sizeprice[i].price)
        listcolor.append(sizeprice[i].color.styletitle)
        listsize.append(sizeprice[i].size.slug)
        
    print("============================")
    # if listcolor[0] == "black" and listsize[0] == "m":
    #     print(listprice[0])
    
    context = {
        "product":product,
        "listprice": listprice,
        "listcolor": listcolor,
        "listsize": listsize,
    }
    return render(request,'shop-single.html',context)

# search , shopbasked fonksiyon, detay yorum 
def ShopBasket(request):
    

    
    context = {}
    return render(request, 'user/shop-basket.html', context)