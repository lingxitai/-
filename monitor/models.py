from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    class Meta:
        verbose_name='用户名'
        verbose_name_plural=verbose_name
class user_qx(models.Model):
    username=models.CharField(max_length=20)
    quanxian=models.CharField(max_length=20)
    yemian=models.CharField(max_length=20)