from django.contrib import admin

from fruits.models import Fruit, Category


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'nutrition', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']