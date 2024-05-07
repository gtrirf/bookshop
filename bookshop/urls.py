from django.urls import path
from . import views

app_name = 'bookshop'

urlpatterns = [
    path('', views.main, name='main'),
    path('authors/', views.get_author, name='get_author'),
    path('authors/<int:pk>/', views.get_author, name='author_detail'),
    path('books/', views.get_books, name='get_books'),
    path('books/<int:pk>/', views.detail, name='book_detail'),
    path('add_books/', views.add_books, name='add_books'),
    path('update_books/<int:pk>/', views.update_books, name='update_books'),
    path('delete_books/<int:pk>/', views.delete_books, name='delete_books'),
]
