from django.urls import path

from . import views

# app_name = "books"

urlpatterns = [
    # auth urls
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    # Book urls
    path("", views.homepage, name="homepage"),
    path("book/<int:book_id>/", views.book_detail, name="book_detail"),
    path("book/add/", views.add_book, name="add_book"),
    path("book/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("book/<int:book_id>/delete/", views.delete_book, name="delete_book"),
    # API urls
    path("api/routes/", views.get_routes, name="api-routes"),  # API routes
    path("api/books/", views.get_books, name="get-books"),  # Get all books
    path("api/books/<int:book_id>/", views.get_book, name="get-book"),  # Get book by ID
]
