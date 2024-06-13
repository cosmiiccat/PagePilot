from django.urls import path 
from . import views 

urlpatterns = [
    path("ensure", views.ensure, name="ensure"),

    path("books/list", views.list_books, name="list-books"),
    path("books/add", views.add_book, name="add-book"),
    path("books/update", views.update_book, name="update-book"),
    path("books/delete", views.delete_book, name="delete-book"),
    path("books/search", views.search_book, name="search-book"),

    path("users/list", views.list_users, name="list-users"),
    path("users/add", views.add_user, name="add-user"),
    path("users/update", views.update_user, name="update-user"),
    path("users/delete", views.delete_user, name="delete-user"),
    path("users/search", views.search_user, name="search-user"),

    path("issue", views.issue_book, name="issue-book"),
    path("return", views.return_book, name="return-book")
]