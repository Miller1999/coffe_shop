# Se crea un superusario usando el ./manage.py createsuperuser, esto porque django cuenta con un sistema de autenticacion

from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "created_at"]
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)
