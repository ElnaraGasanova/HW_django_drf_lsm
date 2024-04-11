from django.urls import path
from courses import views
from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet

app_name = CoursesConfig.name

router = DefaultRouter()
#подключаем набор контроллеров на основе ViewSet
router.register(r'courses', CourseViewSet, basename='courses')

urlspatterns = [
    path('courses/', views.CourseViewSet)
]