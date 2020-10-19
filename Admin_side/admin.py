from django.contrib import admin
from .models import Book,Genre


# Register your models here.

class BookDisplay(admin.ModelAdmin):
    list_display = ['title', 'price', 'desc', 'image', 'available']


admin.site.register(Book, BookDisplay)
admin.site.register(Genre)