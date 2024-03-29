"""ticaret27ocak URL Configuration

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
    path('About/',About, name="About"),
    path('Contact/',Contact, name="Contact"),
    path('Shop/',Shop, name="Shop"),
    path('ShopDetail/<slug>/',ShopDetail, name="ShopDetail"),
    # USER
    path('ShopBasket/', ShopBasket, name='ShopBasket'),
    path('login/', loginUser, name="loginUser"),
    path('register/', registerUser, name="registerUser"),
    path('logout/', logoutUser, name="logoutUser"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
