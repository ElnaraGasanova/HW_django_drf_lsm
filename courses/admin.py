from django.contrib import admin
from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)
