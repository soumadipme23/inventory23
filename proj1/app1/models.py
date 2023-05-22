from django.db import models


class Inventory(models.Model):
    category = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    stock = models.IntegerField()
    doi = models.DateField()

class Req(models.Model):
    faculty = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    vendor = models.CharField(max_length=50)
    date = models.DateTimeField()

class Temp(models.Model):
    faculty = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    total = models.IntegerField()
    stock = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    vendor = models.CharField(max_length=50)
    des = models.CharField(max_length=100)
    jus = models.CharField(max_length=100)
    date = models.DateField()
# Create your models here.
