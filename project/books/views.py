from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import BookForm
from .models import Book
from .serializers import BookSerializer

# Create your views here.


def index(request):
    return render(request, "layout.html")


def loginPage(request):
    # Used in login_or_register to determine page
    page = "login"
    # Check is user is logged in
    if request.user.is_authenticated:
        # Redirect to home if logged in
        return redirect("homepage")

    # Submitted login form
    if request.method == "POST":
        # Get email and password
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        # Try to get user by username
        user = get_object_or_404(User, username=username)

        # Verify password entered matches user password hash
        user = authenticate(request, username=username, password=password)

        # If user was returned
        if user is not None:
            # Login and set cookie
            login(request, user)
            return redirect("homepage")
        else:
            print("Invalid username or passwors")

    # Render login_register page
    context = {"page": page}
    return render(request, "login_register.html", context)


def logoutUser(request):
    # Call user logout function to logout
    logout(request)
    return redirect("homepage")


def registerUser(request):
    # Get UserCreationForm from django
    form = UserCreationForm()

    if request.method == "POST":
        # Pass form data to form
        form = UserCreationForm(request.POST)
        # If no errors in form
        if form.is_valid():
            # Build user object
            user = form.save(commit=False)
            user.username = user.username.lower()
            # Save new user in database
            user.save()
            # Login as new user
            login(request, user)
            # Redirect home
            return redirect("homepage")
        else:
            print("Error in registration")

    # Render register form
    return render(request, "login_register.html", {"form": form})


# Homepage view
def homepage(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, "homepage.html", {"books": books})


# Book detail view
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)  # Get book by id
    can_edit_or_delete = (
        request.user == book.created_by
    )  # Check if the logged-in user created the book
    return render(
        request,
        "book_detail.html",
        {"book": book, "can_edit_or_delete": can_edit_or_delete},
    )


# Add new book view
@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user  # Associate the logged-in user with the book
            book.save()
            messages.success(request, "Book added successfully!")
            return redirect("homepage")
    else:
        form = BookForm()
    return render(request, "add_book.html", {"form": form})


# Edit book view
@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.created_by != request.user:
        messages.error(request, "You are not authorized to edit this book.")
        return redirect("homepage")

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect("book_detail", book_id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, "edit_book.html", {"form": form, "book": book})


# Delete book view
@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.created_by != request.user:
        messages.error(request, "You are not authorized to delete this book.")
        return redirect("homepage")

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect("homepage")

    return render(request, "delete_book.html", {"book": book})


# Get API routes
@api_view(["GET"])
def get_routes(request):
    routes = [
        "GET /api/books/",  # Get list of books
        "GET /api/books/<id>/",  # Get book by ID
    ]
    return Response(routes)


# Get all books
@api_view(["GET"])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# Get book by ID
@api_view(["GET"])
def get_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    return Response(serializer.data)
