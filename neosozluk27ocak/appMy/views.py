from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    sozluks = Sozluk.objects.all()[:5]
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
    
    paginator = Paginator(sozluks, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    sozluks = paginator.get_page(page_number)
    
        
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