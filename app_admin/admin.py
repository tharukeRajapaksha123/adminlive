from django.contrib import admin
from .models import CourseContent, Level, Quiz,QuizItem, Screen,User


# Register your models here.
admin.site.register(Quiz)
admin.site.register(QuizItem)
admin.site.register(User)
admin.site.register(Screen)
admin.site.register(Level)
admin.site.register(CourseContent)


