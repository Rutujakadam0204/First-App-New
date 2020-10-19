from django.shortcuts import render, redirect, HttpResponse
from .forms import SubscriberForm
from .models import Subscriber, Add_to_cart
from Admin_side import models
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def entry(request):
    pass
    return render(request,"index.html")


def register(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        n = request.POST.get("email")
        p = request.POST.get("password")
        if form.is_valid():
            form.save()
            send_mail('About Registration',
                      f'Hii!!! You have successfully registered on Mywebsite.This is your login details \n'
                      f'Username:{n} \n'
                      f'Password:{p}',
                      settings.EMAIL_HOST_USER,
                      [n]
                      )
            return redirect("login")
        else:
            form = SubscriberForm()
    return render(request, "User_register.html", {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            sub = Subscriber.objects.get(email=email, password=password)
            request.session['username'] = sub.email
            request.session['password'] = sub.password
            return redirect("display")
        except Exception:
            HttpResponse("Email is not registered")
    return render(request, "User_Login.html")


def logout(request):
    try:
        del request.session['username']
        del request.session['password']
        return render("entry")
    except Exception:
        pass
    return render(request, "User_Login.html")


def display(request, title=None):
    if request.session['username']:
        if request.session['username']:
            books = models.Book.objects.filter(available=True)
            gen = models.Genre.objects.all()
            sub = Subscriber.objects.get(email=request.session['username'])
            cart = Add_to_cart.objects.filter(owner=sub)
            if title is not None:
                genr = models.Genre.objects.get(title=title)
                books = models.Book.objects.filter(genre=genr)
        else:
            return HttpResponse("Please Login first")
    return render(request, "User_display.html", {'books': books, 'genre': gen, 'cart': cart})


def detail(request, title):
    if request.session['username']:
        book = models.Book.objects.filter(title=title)
    return render(request, "User_Detaibook.html", {"Book": book})


def addtocart(request, title):
    if request.session['username']:
        try:
            if request.session['username']:
                sub = Subscriber.objects.get(email=request.session['username'])
                book = models.Book.objects.get(title=title)
                cart = Add_to_cart()
                cart.owner = sub
                cart.save()
                cart = Add_to_cart.objects.filter(owner=sub)
                for i in cart:
                    i.books.add(book)
                    return redirect('viewcart')
        except Exception as e:
            print(e)
            return redirect("display")
    return render(request, "User_display.html")


def viewCart(request):
    if request.session['username']:
        sub = Subscriber.objects.get(email=request.session['username'])
        cart = Add_to_cart.objects.filter(owner=sub)
    return render(request, "User_Mycart.html", {"mycart": cart})


def removefromcart(request, id):
    if request.session['username']:
        sub = Subscriber.objects.get(email=request.session['username'])
        cart = Add_to_cart.objects.filter(owner=sub)
        for i in cart:
            i.books.remove(id)
            return redirect("viewcart")
    return render(request, "User_Mycart.html")
