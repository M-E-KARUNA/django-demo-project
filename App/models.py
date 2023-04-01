from django.db import models

# Create your models here.
class Student(models.Model):

    roll =models.IntegerField();
    name =models.CharField(max_length=20);
    branch=models.CharField(max_length=5,null=True);



class StudentMark(models.Model):
    name=models.CharField(max_length=10);
    mark=models.IntegerField();

    