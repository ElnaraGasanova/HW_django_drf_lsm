from rest_framework import viewsets, generics
from courses.models import Course
from courses.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    '''Описываем ViewSet для работы с моделью.'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
