"""netflix27ocak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('Netflix/<pid>/', indexBrowse, name="indexBrowse"),
    # USER
    path('Profil/', Browse, name="Browse"), # Profil
    path('ProfilDel/<pid>/', BrowseDel, name="BrowseDel"), # Profil Sil
    path('Hesap/<pid>/', Hesap, name="Hesap"), # Hesap Ayarları
    path('Login/', loginUser, name="loginUser"), # Giriş Yap
    path('Logout/', logoutUser, name="logoutUser"), # Çıkış Yap
    path('Register/', registerUser, name="registerUser"), # Kaydol
    
] + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
