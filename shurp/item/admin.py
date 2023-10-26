from django.contrib import admin

# import models
from .models import Category, Item

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)