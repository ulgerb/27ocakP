from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# Create your views here.


@login_required(login_url="/")
def Browse(request):
    
    context={"title":"Profiller"}
    profils = Profil.objects.filter(user=request.user)
    
    if request.method == "POST":
        if request.POST.get("button") == "buttonProfil":
            profilid = request.POST.get("profilid")
            profil = profils.get(id=profilid) # profili getir
            
            name = request.POST.get("name")
            image = request.FILES.get("image")
            if image is None:
                image = profil.image
            
            profil.name = name
            profil.image = image
            profil.save()
            return redirect("Browse")
    
    if len(profils)<4:
        if request.method == "POST":
            if request.POST.get("button") == "makeprofil":
                name = request.POST.get("name")
                image = request.FILES.get("image")
                if image is None:
                    image = "profil/car1.jpg"
                    
                
                profil = Profil(name=name,image=image, user = request.user)
                profil.save()
                return redirect('Browse')
    elif len(profils)>4:
        profils.last().delete()
        return redirect('Browse')
    
    context.update({
        "profils": profils,
    })
    return render(request,"user/browse.html",context)

def BrowseDel(request,pid):
    profil = Profil.objects.get(id=pid)
    profil.delete()
    return redirect('Browse')

def Hesap(request,pid):
    context={"title":"Hesap Ayarları"}
    profils = Profil.objects.filter(user = request.user)
    profil = Profil.objects.get(id=pid)
    userinfo = UserInfo.objects.get(user=request.user)
    user = User.objects.get(username = request.user)
    # HESAP AYARLARI
    if request.method == "POST":
        
        if request.POST.get("formbutton") == "emailChange":
            email = request.POST.get("email")
            user.email = email
            user.save()
            return redirect("/Hesap/" + pid + "/")
        elif request.POST.get("formbutton") == "passwordChange":
            oldpassword = request.POST.get("password")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if password1 == password2:
                if user.check_password(oldpassword):
                    userinfo.password = password1
                    userinfo.save()
                    user.set_password(password1)
                    user.save()

            return redirect("/Login/")
    
    context.update({
        "profil":profil,
        "profils":profils,
        "userinfo": userinfo,
    })
    return render(request,"user/hesap.html",context)

def loginUser(request): # Giriş Yap
    context={"title":"Giriş Yap"} 

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username = username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('Browse')
        else:
            messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
            return redirect("loginUser")
    
    return render(request,"user/login.html",context)

def logoutUser(request): # Çıkış Yap
    logout(request)
    return redirect('index')

def registerUser(request):
    context={"title":"Kaydol"}

    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(first_name=name,last_name=surname, 
                                                    username=username, email=email, password=password1)
                    user.save()

                    userinfo = UserInfo(user=user, password=password1 )
                    userinfo.save()
                    
                    messages.success(request, "Kaydınız başarıyla oluşturulmuştur...")
                    return redirect("loginUser")
                else:
                    messages.warning(request, "Bu email zaten kullanılıyor!")
                    return redirect("registerUser")
            else:
                messages.warning(request, "Bu kullanıcı adı zaten alınmış!")
                return redirect("registerUser")
        else:
            messages.warning(request, "Şifreler aynı değil!")
            return redirect("registerUser")
            
    return render(request,'user/register.html',context)