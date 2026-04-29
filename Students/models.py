from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    major = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)