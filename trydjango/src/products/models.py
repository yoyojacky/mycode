from django.db import models

# Create your models here.
class ProductInStorage(models.Model):
    storageTime = models.DateTimeField("入库时间",auto_now=True)
    productSKU = models.CharField("产品SKU",max_length=80, null=False)
    productName = models.CharField("产品名称",max_length=120, null=False)
    price = models.DecimalField("成本价",decimal_places=2,max_digits=100000, default=0)
    weight = models.DecimalField("产品重量",decimal_places=2,max_digits=100000, default=0)
    storageQuantity = models.DecimalField("入库数量",decimal_places=2,max_digits=100000, default=0)
    onlineStatus = models.BooleanField("是否上架", default=True)

    def __str__(self):
        return self.productSKU
    
    class Meta:
        verbose_name = '产品入库'
        verbose_name_plural = '产品入库'


class ProductOutStorage(models.Model):
    storageTime = models.DateTimeField("出库时间",auto_now=True)
    productSKU = models.CharField("产品SKU",max_length=80, null=False)
    productName = models.CharField("产品名称",max_length=120, null=False)
    storageQuantity = models.DecimalField("出库数量",decimal_places=2,max_digits=100000, default=0)
    remainQuantity = models.DecimalField("库存余量",decimal_places=2,max_digits=100000, default=0)
    onlineStatus = models.BooleanField("是否上架", default=True)

    def __str__(self):
        return self.productSKU

    class Meta:
        verbose_name = '产品出库'
        verbose_name_plural = '产品出库'
