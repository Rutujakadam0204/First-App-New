from django.shortcuts import render, redirect
from . import forms as f
from .models import Book, Super_user
from django.contrib.auth import authenticate


# Create your views here.


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            super_user = Super_user.objects.get(username=username, password=password)
            request.session['username'] = super_user.username
            request.session['password'] = super_user.password
            return redirect("Admin_display")
        except Exception:
            return redirect("Admin_login")
    return render(request, "Admin_login.html")


def logout(request):
    try:
        del request.session['username']
        del request.session['password']
        return redirect("Admin_login")
    except Exception:
        pass
    return render(request, "Admin_Display.html")


def add_book(request):
    if request.session['username']:
        form = f.BookForm()
        if request.method == "POST":
            print("method")
            form = f.BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                book = Book.objects.filter(title=request.POST.get("title"))
                grn = request.POST.getlist("genre")
                for i in book:
                    i.genre.add(*grn)
                return redirect("add_book")
            else:
                print('else')
    return render(request, "Admin_add.html", {'form': form})


def display(request):
    if request.session['username']:
        book_disp = Book.objects.all()
    return render(request, "Admin_Display.html", {'book_disp': book_disp})


def add_genre(request):
    if request.session['username']:
        form = f.GenreForm()
        if request.method == 'POST':
            form = f.GenreForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_genre')
    return render(request, "Admin_add_genre.html", {'form': form})


def edit_book(request, title):
    if request.session['username']:
        book = Book.objects.get(title=title)
        form = f.BookForm(instance=book)
        if request.method == "POST":
            form = f.BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return redirect("Admin_display")
    return render(request, "Admin_edit.html", {'book': book, 'form': form})


def delete_book(request, id):
    if request.session['username']:
        try:
            book = Book.objects.filter(id=id)
            book.delete()
            return redirect("Admin_display")
        except Exception:
            return redirect("Admin_display")
    return render(request, "Admin_Display.html")
