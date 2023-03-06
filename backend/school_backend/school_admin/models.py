from django.db import models

# Create your models here.
class Admin(models.Model):
    a_username = models.CharField(max_length=30)
    a_password = models.CharField(max_length=30)

    class Meta:
        db_table = 'admin_tb'