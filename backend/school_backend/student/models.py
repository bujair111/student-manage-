from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=100)
    s_age = models.CharField(max_length=20)
    s_gender = models.CharField(max_length=200)
    s_email = models.CharField(max_length=100)
    s_phone = models.CharField(max_length=200)
    s_username =models.CharField(max_length=100)
    s_password = models.CharField(max_length=50)


    class Meta:
        db_table = 'student_tb'