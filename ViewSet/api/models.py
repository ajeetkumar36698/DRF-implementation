from django.db import models

class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    email=models.CharField(max_length=100)
