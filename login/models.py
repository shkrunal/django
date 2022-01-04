from django.db import models

# Create your models here.


class Member(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(default='')
    phone=models.IntegerField(default='')
    password=models.CharField(max_length=19)
    cpassword=models.CharField(max_length=19,default='')

    def __str__(self):
        return self.username


