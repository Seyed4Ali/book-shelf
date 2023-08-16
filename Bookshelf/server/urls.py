from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register_user'),
    path('users_list/', views.user_list, name='user_list'),
    path('books_list/', views.book_list, name='book_list'),
    path('create/', views.create_book, name='create_book'),
    path('update/<int:pk>/', views.update_book, name='update_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),

]