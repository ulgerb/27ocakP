from django.shortcuts import render
from appUser.models import *

# Create your views here.


def index(request):
    context = {"title":"Anasayfa"}
    return render(request,'index.html',context)

def indexBrowse(request,pid):
    context = {"title":"Netflix"}
    profil = Profil.objects.get(id=pid)

    context.update({
        "profil": profil,
    })
    return render(request,'browse-index.html',context)