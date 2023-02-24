from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

def index(request):
    return render(request,'index.html')

def Portfolio(request):
    posts = Post.objects.all()
    categorys = Category.objects.all()
    
    context = {
        "posts": posts,
        "categorys":categorys,
    }
    return render(request, 'portfolio.html', context)

def Detail(request,pid):
    post = get_object_or_404(Post,id=pid)
    context = {
        "post":post,
    }
    return render(request,'portfolio-details.html',context)

def innerPage(request):
    return render(request,'inner-page.html')

# ======= USER =======
def loginUser(request):
    context = {}
    # html formu düzenledikten sonra, request.methodu kontrol etmem lazım
    # request.POST ile gelen bilgileri değişkenlere kaydet,
    # girilen bilgiler SQL için yada DATA da olup olmadığını kontrol ettir,
    # eğer böyle bir kullanıcı varsa giriş yapabilir
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password) # eğer varsa bilgi gider, yoksa None değeri gönderir
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            context.update({"hata":"Kullanıcı adı veya şifre yanlış!!"})

            
    return render(request,'user/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


def registerUser(request):
    context = {}

    print(User.objects.get(username="oguzhan").email)
    
    # şifrelerin aynı olması
    # aynı username sahip kullanıcı bulunamaz
    # aynı maile sahip kullanıcı bulunamaz
    
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        # şifreler aynı olucak, kullanıcı adı daha önceden kullanılmamış olmalı, email @ işareti olucak
        # email daha önceden kullanılmamalı, şifre içinde numara bulunsun büyük harf,
        
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, 
                                                    password=password1,
                                                    email=email, 
                                                    first_name=name, 
                                                    last_name=surname)
                    user.save()
                    return redirect('loginUser')
                else:
                    context.update({"hata":"Bu E-mail zaten kullanılıyor!"})
            else:
                context.update({"hata":"Bu kullanıcı adı zaten alınmış!"})
        else:
            context.update({"hata":"Şifreler aynı değil!!"})
            
    
    return render(request, 'user/register.html', context)


def changePasswordUser(request):
    context = {}
    # request.user # girişli olan kullanıcıyı verir
    
    if request.method == "POST":
        password = request.POST["password"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        user = User.objects.get(username=request.user) # girişli olan kullanıcıyı getir

        if user.check_password(password): # eski parolayı kontrol et
            if password2 == password1: # yeni parolalar birbirine eşit mi?
                user.set_password(password1) # parolayı değiştir
                user.save() # userı kaydet
                logout(request) # userı sistemden çış yaptırt
                return redirect('/login/') # login sayfasına yönlendir
            else:
                context.update({"hata":"Şifreler aynı değil!"}) # hata mesajı
        else:
            context.update({"hata":"Şuanki şifrenizi yanlış girdiniz"})
            
    
    return render(request, 'user/change-password.html', context)

def profilUser(request):
    context={}
    user = User.objects.get(username = request.user)
    userinfo = UserInfo.objects.get(user=user)
    
    print(userinfo.status.all())
    
    if request.method=="POST": # methodun post olduğunu doğrula
        # ___EMAİL___
        if request.POST["formbutton"] == "emailChange": # formdan gelen butonu kontrol et
            password = request.POST["password"] # parolayı değişkene çek
            if user.check_password(password): # parolayı kontrol et
                email = request.POST["email"] # emaili çek
                user.email = email # emaili değiştir
                user.save() # kullanıcıyı kaydet
                return redirect('profilUser') # sayfayı resetle, aynı sayfayı tekrar yönlendir

    context.update({
        "user":user,
        "userinfo":userinfo,
    })
    return render(request,'user/profil.html',context)