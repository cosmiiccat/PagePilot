from django.urls import path 
from . import views 

urlpatterns = [
    path("ensure", views.ensure, name="ensure"),
    path("books/list", views.list_books, name="list-books"),
    path("books/add", views.add_book, name="add-book"),
    path("books/update", views.update_book, name="update-book"),
    path("books/delete", views.delete_book, name="delete-book"),
    path("books/search", views.search_book, name="search-book"),
]