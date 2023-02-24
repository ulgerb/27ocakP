from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title','id','post_url')
    list_filter = ('date_now','category__title')
    search_fields = ('title',)
    ordering = ('date_now',)
   



# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Contact)

# USER
admin.site.register(UserInfo)
admin.site.register(UserInfoStatus)