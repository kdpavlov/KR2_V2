from django.contrib import admin
from .models import StudyRecord
# Register your models here.
@admin.register(StudyRecord)
class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'score', 'date']
    search_fields = ['name', 'course']
    list_filter = ['course']