from django.contrib import admin
from django.contrib import admin
from .models import Page, Student, Management, Person, Program
from django.utils.html import format_html
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

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'photo_preview')
    search_fields = ('full_name', 'email', 'phone', 'role')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height: 100px;" />', obj.photo.url)
        return ""
    photo_preview.short_description = 'Фото'

admin.site.register(Management)
admin.site.register(Program)
