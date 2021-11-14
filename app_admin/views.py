from django.shortcuts import render
from rest_framework import serializers
#from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_admin.models import CourseContent, Level, Quiz, Screen
from app_admin.serializers import CourseContentSerializer, LevelSerializer, QuizSerializer, ScreenSerializer


# Create your views here.
@api_view(['GET'])
# Create your views here.
def apiOverview(request):
    api_urls = {       
        'Get Levels' : '/get-level/s',
        'Get Screens' : '/get-screens/',
        'Get Quiz Item' : '/get-quiz-item/<str:pk>'
        
    }
    return Response(api_urls)

#get all the levels from db
@api_view(['GET'])
def levelList(request):
    levels = Level.objects.all()
    searializer = LevelSerializer(levels,many=True) 
    return Response(searializer.data)

#get screens from db
@api_view(['GET'])
def getScreens(request,pk):
    screen = Screen.objects.get(id=int(pk))
    searializer = ScreenSerializer(screen,many=False) 
    return Response(searializer.data)

#get quiz item from db
@api_view(['GET'])
def getQuiz(request,pk):
    quiz = Quiz.objects.get(id=int(pk))
    serializer = QuizSerializer(quiz,many=False)
    return Response(serializer.data)

#get course content from db
@api_view(['GET'])
def getCourseContent(request,pk):
    content = CourseContent.objects.get(id=int(pk))
    serializer = CourseContentSerializer(content,many=False)
    return Response(serializer.data)
