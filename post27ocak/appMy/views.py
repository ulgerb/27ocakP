from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

def index(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        title = request.POST["title"]
        text = request.POST["text"]
        
        contact = Contact(name=name,email=email,title=title,text=text)
        contact.save()
        return HttpResponseRedirect("/#contact")
    
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
                    
                    userinfo = UserInfo(user=user, password=password1)
                    userinfo.save()
                    
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
    
    if request.method=="POST": # methodun post olduğunu doğrula
        # ___PROFİL___
        if request.POST["formbutton"] == "profilChange":  # formdan gelen butonu kontrol et
            password = request.POST["password"]
            if user.check_password(password):  # parolayı kontrol et
                username = request.POST["username"]  # kullanıcı çek
                job = request.POST["job"]  # iş çek
                image = request.FILES["image"]
                
                user.username = username
                user.save()
                userinfo.job = job
                userinfo.image = image
                userinfo.save()
            
                # user.save()  # kullanıcıyı kaydet
                # sayfayı resetle, aynı sayfayı tekrar yönlendir
                return redirect('profilUser')
            
            
            
            
           
        
        # ___NAME___
        if request.POST["formbutton"] == "nameChange":  # formdan gelen butonu kontrol et
            name = request.POST["name"]  # emaili çek
            surname = request.POST["surname"]  # emaili çek
            
            user.first_name = name  # emaili değiştir
            user.last_name = surname  # emaili değiştir
            user.save()  # kullanıcıyı kaydet
            # sayfayı resetle, aynı sayfayı tekrar yönlendir
            return redirect('profilUser')
            
        # ___EMAİL___
        if request.POST["formbutton"] == "emailChange": # formdan gelen butonu kontrol et
            password = request.POST["password"] # parolayı değişkene çek
            if user.check_password(password): # parolayı kontrol et
                email = request.POST["email"] # emaili çek
                user.email = email # emaili değiştir
                user.save() # kullanıcıyı kaydet
                return redirect('profilUser') # sayfayı resetle, aynı sayfayı tekrar yönlendir
        # ___PHONE___
        if request.POST["formbutton"] == "telChange":  # formdan gelen butonu kontrol et
            password = request.POST["password"]  # parolayı değişkene çek
            if user.check_password(password):  # parolayı kontrol et
                tel = request.POST["tel"]  # tel çek
                userinfo.phone = tel  # tel değiştir
                userinfo.save()  # kullanıcıyı kaydet
                # sayfayı resetle, aynı sayfayı tekrar yönlendir
                return redirect('profilUser')
        
        # ___ADDRESS___
        if request.POST["formbutton"] == "addressChange":  # formdan gelen butonu kontrol et
            address = request.POST["address"]  # tel çek
            userinfo.adress = address  # tel değiştir
            userinfo.save()  # kullanıcıyı kaydet
            # sayfayı resetle, aynı sayfayı tekrar yönlendir
            return redirect('profilUser')
            
                
        # ___STATU___
        if request.POST["formbutton"] == "formStatu":
            title = request.POST["title"]
            statu = request.POST["statu"]
            userstatu = UserInfoStatus(title=title,statu=statu,user=request.user)
            userstatu.save()
            
            userinfo.status.add(userstatu)
            userinfo.save()
            return redirect("profilUser")
            
    context.update({
        "user":user,
        "userinfo":userinfo,
    })
    return render(request,'user/profil.html',context)

def deleteStatu(request,sid):
    statu = UserInfoStatus.objects.get(id=sid)
    statu.delete()
    return redirect("profilUser")
    