from django.db import models

from login.models import Member

# Create your models here.


class product(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default='')
    offpri=models.IntegerField(default='')
    qty=models.IntegerField(default='')
    desc=models.TextField(default='')
    img=models.ImageField(upload_to='pro_img',blank=True)
    def __str__(self):
        return self.name


class man(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default='')
    offpri=models.IntegerField(default='')
    image=models.ImageField(upload_to="Mens/",blank=True)
    qty=models.IntegerField(default='')
    desc=models.TextField(default='')
    def __str__(self):
        return self.name


class woman(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default='')
    offpri=models.IntegerField(default='')
    image=models.ImageField(upload_to="women/",blank=True)
    qty=models.IntegerField(default='')
    desc=models.TextField(default='')
    def __str__(self):
        return self.name


class body(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default='')
    offpri=models.IntegerField(default='')
    image=models.ImageField(upload_to="body/",blank=True)
    qty=models.IntegerField(default='')
    desc=models.TextField(default='')
    def __str__(self):
        return self.name


class cosmetic(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default='')
    offpri=models.IntegerField(default='')
    image=models.ImageField(upload_to="cosmetic/",blank=True)
    qty=models.IntegerField(default='')
    desc=models.TextField(default='')
    def __str__(self):
        return self.name


class accesory(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default='')
    offpri=models.IntegerField(default='')
    image=models.ImageField(upload_to="accesory/",blank=True)
    qty=models.IntegerField(default='')
    desc=models.TextField(default='')
    def __str__(self):
        return self.name


class offers(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default='')
    offpri=models.IntegerField(default='')
    image=models.ImageField(upload_to="offers/",blank=True)
    qty=models.IntegerField(default='')
    desc=models.TextField(default='')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(Member,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField()