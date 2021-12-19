from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_display_links = ('id', 'name', 'user')
    search_fields = ('name', 'user',)

    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'user', None) is None:
    #         obj.user = request.user
    #     obj.save()


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'board')
    list_display_links = ('id', 'name', 'board')
    search_fields = ('name', 'board')

    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'board', None) is None:
    #         obj.board = Board.objects.get(request.user.pk).pk
    #     obj.save()


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'deadline', 'photo', 'column')
    list_display_links = ( 'name', 'deadline', 'column')
    search_fields = ('name', 'column')

admin.site.register(Board, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Card, CardAdmin)

# Register your models here.
