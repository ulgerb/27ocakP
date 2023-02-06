from django.contrib import admin
# from appMy.models import *
from .models import *
# SQL'deki, models tabloları görüntülemek için tanımlarız


admin.site.register(Card)
admin.site.register(Product)