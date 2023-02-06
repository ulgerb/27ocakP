from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    sozluks = Sozluk.objects.all()
    # Side nav
    sozluks_new = Sozluk.objects.all().order_by("-date_now")[:3]
    sozluks_random = Sozluk.objects.all().order_by("?")[:3]
    categorys = Category.objects.all()
    
    context={
        "sozluks": sozluks,
        # Side nav 
        "sozluks_new": sozluks_new,
        "sozluks_random": sozluks_random,
        "categorys":categorys,
    }
    return render(request,'index.html',context)

def Detail(request,id):
    # bu sayfada 1 obje gönderilmeli
    sozluk = Sozluk.objects.get(id=id)
    # Side nav
    sozluks_new = Sozluk.objects.all().order_by("-date_now")[:3]
    sozluks_random = Sozluk.objects.all().order_by("?")[:3]
    categorys = Category.objects.all()
    
    context={
        "sozluk": sozluk,
        # Side nav
        "sozluks_new": sozluks_new,
        "sozluks_random": sozluks_random,
        "categorys": categorys,
    }
    return render(request, 'detail.html',context)

def allPost(request,categoryid="all"):
    
    if categoryid == "all":
        sozluks = Sozluk.objects.all()
    else:
        sozluks = Sozluk.objects.filter(category=categoryid)
        
    # Side nav
    sozluks_new = Sozluk.objects.all().order_by("-date_now")[:3]
    sozluks_random = Sozluk.objects.all().order_by("?")[:3]
    categorys = Category.objects.all()
    
    context={
        "sozluks": sozluks,
        # Side nav
        "sozluks_new": sozluks_new,
        "sozluks_random": sozluks_random,
        "categorys": categorys,
    }
    return render(request,'allPost.html',context)