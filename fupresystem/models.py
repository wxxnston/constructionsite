from django.db import models

# Create your models here.

class response(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    company=models.CharField(max_length=100)

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)