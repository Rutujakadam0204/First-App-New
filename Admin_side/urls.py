from django.urls import path
from . import views


urlpatterns = [
                  path('', views.admin_login, name='Admin_login'),
                  path('logout', views.logout, name='Admin_logout'),
                  path('add_book', views.add_book, name='add_book'),
                  path('genre', views.add_genre, name='add_genre'),
                  path('display', views.display, name='Admin_display'),
                  path('delete_book/<int:id>', views.delete_book, name='delete_book'),
                  path('edit_book/<str:title>', views.edit_book, name='edit_book'),
              ]
