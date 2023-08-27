from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

class Cart(models.Model):
    total = models.IntegerField()
    items = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    age = models.IntegerField()
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)


class Manager(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    age = models.IntegerField()


class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

class Delivery_Crew(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    age = models.IntegerField()


class People(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    category = models.CharField(max_length=50)

