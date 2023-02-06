from django.shortcuts import render
from .models import *

def index(request):
    cards = Card.objects.all() # tüm kartları gönderir
    
    context={
        "title": "Anasayfa Cartlar",
        "pagelook":"Bir Sayfayı Görüntülemenin Yoluuu",
        "cards": cards,
    }
    return render(request,'index.html',context)

def About(request,cardid):
    products = Product.objects.all()
    prod1 = Product.objects.get(id=cardid) # get() yalnızca 1 eleman çeker
    prod2 = Product.objects.get(title="Telefon")
    products2 = Product.objects.all()[:3]
    cards_filter1 = Card.objects.filter(active=True)
    cards_apple = Card.objects.filter(brand ="Apple")
    cards_samsung = Card.objects.filter(brand ="Samsung")
    
    context={
        "products":products,
        "prod1": prod1,
        "prod2":prod2,
        "products2":products2,
        "cards_filter1":cards_filter1,
        "cards_apple":cards_apple,
        "cards_samsung":cards_samsung,
    }
    return render(request,'about.html',context)

def Contact(request):
    
    return render(request,'contact.html')

def allProduct(request):
    cards = Card.objects.all().order_by("-id")
    cards_active = Card.objects.filter(active=True)
    cards_active_non = Card.objects.filter(active=False)
    cards_r = Card.objects.all().order_by("?")[:4] # rastgele getirmek için order_by("?")
    # cards_r = cards_r[:4]
    context = {
        "kartlar":cards,
        "cards_active": cards_active,
        "cards_active_non": cards_active_non,
        "cards_r": cards_r,
    }
    return render(request, "allproduct.html",context)
