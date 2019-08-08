from django.contrib import admin

# Register your models here.
from .models import ProductInStorage, ProductOutStorage

admin.site.register(ProductInStorage)
admin.site.register(ProductOutStorage)
