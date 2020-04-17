from django.db import models

# Create your models here.

class Users(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Password = models.CharField(max_length=8)
    Phone = models.IntegerField()



class Products(models.Model):
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=1000)
    img = models.ImageField()
    

