from django.db import models
from Admin_side.models import Book


# Create your models here.


class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.email


class Add_to_cart(models.Model):
    owner = models.ForeignKey(Subscriber, on_delete=Subscriber)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.books