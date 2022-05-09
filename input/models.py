from django.db import models

# Create your models here.

class feedback(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.EmailField(default='')
    message=models.TextField(max_length=100)

    def __str__(self):
        return self.fname

class contect(models.Model):
    name=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.EmailField()
    phone=models.IntegerField()
    coments=models.TextField(max_length=100)
    def __str__(self):
        return self.name

class cal(models.Model):
    val1=models.IntegerField(default='')
    val2=models.IntegerField(default='')
    answer=models.PositiveIntegerField(default='')