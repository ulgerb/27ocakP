from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''

    list_display = ('user','name','id')
    list_filter = ('user','name')
    
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''

    list_display = ('user', 'phone_number', 'id')
    list_filter = ('user','phone_number')