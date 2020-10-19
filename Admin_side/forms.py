from django.forms import ModelForm
from .models import Book,Genre


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
