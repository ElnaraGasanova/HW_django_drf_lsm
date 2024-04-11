from rest_framework import serializers
from lessons.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор.'''
    class Meta:
        model = Lesson
        fields = '__all__'
