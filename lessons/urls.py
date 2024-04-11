from django.urls import path
from lessons.apps import LessonsConfig
from rest_framework.routers import DefaultRouter
from lessons.views import (LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView,
                           LessonDestroyAPIView)


app_name = LessonsConfig.name

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_get'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lessons_delete'),
]
