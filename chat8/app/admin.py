from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Chat)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'time', 'group')


@admin.register(Group)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')