from django.contrib import admin
from django.contrib import admin
from .models import Page, Student
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated')
    search_fields = ('title',)
    ordering = ('-updated',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'score')
    search_fields = ('full_name', 'email')
    ordering = ('-score',)