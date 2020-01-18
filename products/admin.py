from django.contrib import admin

from .models import Ingredient, Category

admin.site.register(Ingredient)
admin.site.register(Category)
