"""post27ocak URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

from appMy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('Home/Portfolio/', Portfolio, name='Portfolio'),
    path('Home/Portfolio/Detail/<pid>/', Detail, name='Detail'),
    path('inner/', innerPage,name='innerPage'),
    
    # USER
    path('login/', loginUser, name='loginUser'), # Giriş Yap
    path('logout/', logoutUser, name='logoutUser'), # Çıkış Yap
    path('register/', registerUser, name='registerUser'), # Kaydol
    path('changePassword/', changePasswordUser, name='changePasswordUser'), # Parola değiştir
    path('profil/', profilUser, name='profilUser'), # Kullanıcı profili
    path('profil/deleteStatu/<sid>/', deleteStatu, name="deleteStatu"), # Yetenek Silme
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
