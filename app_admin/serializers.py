from rest_framework import serializers
from .models import Level, Quiz, QuizItem, Screen ,CourseContent

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuizItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizItem
        fields = '__all__'

class CourseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent 
        fields = '__all__'
