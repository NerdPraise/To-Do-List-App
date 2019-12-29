from django.contrib import admin
from .models import Category, Todo, CompletedList, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(CompletedList)