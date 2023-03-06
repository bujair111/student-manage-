from django.db import models

# Create your models here.
class Teacher(models.Model) :
    t_name = models.CharField(max_length=30)
    t_gender = models.CharField(max_length=15)
    t_age = models.IntegerField()
    t_subject = models.CharField(max_length=30)
    t_email = models.CharField(max_length=50)
    t_phone = models.BigIntegerField()
    t_pass = models.CharField(max_length=30)

    class Meta:
        db_table = 'teacher_tb'

