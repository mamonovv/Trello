from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *


class BoardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'board')
    list_display_links = ('id', 'name', 'board')
    search_fields = ('name', 'board')


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'deadline', 'photo', 'column', 'board')
    list_display_links = ( 'name', 'deadline', 'column', 'board')
    search_fields = ('name', 'board')

admin.site.register(Boards, BoardsAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Card, CardAdmin)

# Register your models here.
