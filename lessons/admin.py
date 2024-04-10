from django.contrib import admin
from lessons.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'course',)
    list_filter = ('course',)
    search_fields = ('course',)
