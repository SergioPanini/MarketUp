from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name="owner's name product")
    email = models.EmailField(verbose_name="owner's email")
    password = models.CharField(max_length=8, verbose_name="owner's password")
    phone = models.IntegerField()


class Products(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="owner")
    name = models.CharField(max_length=255, verbose_name="product's name")
    description = models.CharField(max_length=1000, verbose_name="product's descriptions")
    img = models.ImageField()