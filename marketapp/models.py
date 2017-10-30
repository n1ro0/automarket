from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)


class Owner(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    photo = models.ImageField(default="static/cat.jpeg", upload_to="ownerphotos")


class CarAd(models.Model):
    title = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    owner = models.ForeignKey(Owner)
    prize = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    photo = models.ImageField(default="static/cat.jpeg", upload_to="ownerphotos")


class Offer(models.Model):
    text = models.TextField(max_length=1000)
    car = models.ForeignKey(CarAd)

# Create your models here.
