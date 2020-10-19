from django.urls import path
from . import views
from Admin_side.views import admin_login

urlpatterns = [
    path('', views.entry, name='entry'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('display', views.display, name='display'),
    path('Admin_side', admin_login, name='login1'),
    path('viewcart', views.viewCart, name='viewcart'),
    path('logout', views.logout, name='logout'),
    path('remove/<int:id>', views.removefromcart, name='remove'),
    path('mycart/<str:title>', views.addtocart, name='mycart'),
    path('<str:title>', views.detail, name='detail'),
    path('display/<str:title>', views.display, name='display_title'),
]
