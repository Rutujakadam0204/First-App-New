from django.db import models


# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/')
    price = models.PositiveIntegerField()
    genre = models.ManyToManyField(Genre)
    desc = models.TextField(max_length=1000)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.title, self.genre


class Super_user(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
