from django.contrib import admin

# Register your models here.
from .models import Author,Book,SaleItem
Models = [Author,Book,SaleItem]
admin.site.register(Models)