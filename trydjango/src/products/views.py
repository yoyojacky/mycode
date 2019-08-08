from django.shortcuts import render
from .models import ProductInStorage, ProductOutStorage

# Create your views here.
def productList():
    product_info = ProductInStorage.objects.all()
    context = {
            "storageTime":product_info.storageTime,
            "productSKU":product_info.productSKU,
            "productName":product_info.productName,
            "Price":product_info.price,
            "weight":product_info.weight,
            "storageQuantity":product_info.storageQuantity,
            "onlineStatus":product_info.onlineStatus,
            }
