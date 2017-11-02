from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Owner(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    photo = models.ImageField(default="ownerphotos/default.png", upload_to="ownerphotos")

    def __str__(self):
        return self.name


class CarAd(models.Model):
    title = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    owner = models.ForeignKey(Owner)
    prize = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category, related_name="carads")
    photo = models.ImageField(default="ownerphotos/default.png", upload_to="ownerphotos")

    def __str__(self):
        return self.title


class Offer(models.Model):
    text = models.TextField(max_length=1000)
    car = models.ForeignKey(CarAd)

    def __str__(self):
        return self.text

# Create your models here.
