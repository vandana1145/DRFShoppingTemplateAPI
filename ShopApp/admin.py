from django.contrib import admin
from .models import Category, Product, Choice

# Register your models here.

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Choice)