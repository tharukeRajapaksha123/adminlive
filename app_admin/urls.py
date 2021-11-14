from django.urls import path
from . import views


urlpatterns = [
    path('',views.apiOverview,name="home"),
    path('levels',views.levelList,name="level"),
    path('screen/<str:pk>',views.getScreens,name="screen"),
    path('quiz/<str:pk>',views.getQuiz,name="quiz"),
    path('course-content/<str:pk>',views.getCourseContent,name="course-content"),
]