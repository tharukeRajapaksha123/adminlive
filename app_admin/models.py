from django.db import models
import random

levels = ((1,"Level 1"),(2,"Level 2"),(3,"Level 3")) 

answerTypes = ((1,"Short Text"),(2,"Paragraph"),(3,"Check Box"))

layouts = ((1,"Layout 1"),(2,"Layout 2"),(3,"Layout 3"),(4,"Layout 4"),(5,"Layout 5"),)


# Create your models here.
class Level(models.Model):
    name = models.CharField(max_length=200,null=False)
    description = models.TextField(max_length= 500)
    price = models.FloatField(null=False)
    
    def __str__(self) :
         return self.name


class Screen(models.Model):
    name =models.CharField(max_length=100,null=False)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Quiz(models.Model):
    name = models.CharField(max_length=200,null=False,default="Quiz 01")
    level = models.IntegerField(choices=levels)
    timePeriod = models.IntegerField()
    screen = models.OneToOneField(Screen,on_delete=models.CASCADE)     
    def __str__(self) :
         return self.name


class QuizItem (models.Model):
    question = models.CharField(max_length=5000,null=False)
    answer = models.CharField(max_length=5000, null=False)
    quizId =  models.ForeignKey(Quiz,on_delete=models.CASCADE)
    answerType = models.IntegerField(choices=answerTypes)
    option1 = models.CharField(null=-True,max_length=100)
    option2 = models.CharField(null=-True,max_length=100)
    option3 = models.CharField(null=-True,max_length=100)
    option4 = models.CharField(null=True,max_length=100)
    def __str__(self) :
         return self.question

class CourseContent(models.Model):
    title = models.CharField(max_length=200,null=False)
    paragraph = models.CharField(max_length=5000)
    image = models.URLField(max_length=500)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    screen = models.OneToOneField(Screen,on_delete=models.CASCADE,)
    layout = models.IntegerField(choices=layouts,default=1)
    def __str__(self):
        return self.title

class User(models.Model):
    email = models.CharField(max_length=100,null=False)
    level = models.IntegerField(null=False,default=1)
    name = models.CharField(max_length=500,null=False)


    def __str__(self) :
         return self.name


    
        
