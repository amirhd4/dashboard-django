from django.contrib import admin
from django.db import models

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=80)
    product_price = models.CharField(max_length=16)
    product_description = models.TextField()
    product_date = models.DateTimeField(null=False, blank=False)

class ProductChanges(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(null=False,blank=False)
    product_price = models.CharField(max_length=16, null=False, blank=False)
    product_date = models.DateTimeField(null=False, blank=False)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("product_id", "product_name", "product_price", "product_description", "product_date")
class ProductChangesAdmin(admin.ModelAdmin):
    list_display = ("id", "product_id", "product_price", "product_date")

admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductChanges, ProductChangesAdmin)