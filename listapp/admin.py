from django.contrib import admin
from .models import Category, Todo, CompletedList

# Register your models here.
admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(CompletedList)