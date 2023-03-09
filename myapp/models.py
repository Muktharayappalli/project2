from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True,blank=True)
    Mobile = models.IntegerField(null=True, blank=True)

class employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email= models.EmailField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)

class registerdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)

class imagedb(models.Model):
    name = models.CharField(max_length=30, null=True,blank=True)
    Image = models.ImageField(upload_to="profile",null=True,blank=True)


