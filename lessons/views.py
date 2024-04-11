from rest_framework import generics
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    '''Описываем контроллеры на основе дженерик.'''
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    '''Описываем контроллеры на основе дженерик.'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()