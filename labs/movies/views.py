from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Movie, Review
from .forms import MovieForm, ReviewForm

# Create your views here.

movies_array = [
    {"id": 1, "name": "Monkey Kind"},
    {"id": 2, "name": "Land of Apes"},
    {"id": 3, "name": "Pirates of the Arabia"},
]


def index(request):
    movies = get_list_or_404(Movie)

    context = {"page_title": "Movies", "movies": movies}

    return render(request, "movies/homepage.html", context)


def loginPage(request):
    # Used in login_or_register to determine page
    page = "login"
    # Check is user is logged in
    if request.user.is_authenticated:
        # Redirect to home if logged in
        return redirect("movies:index")

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
            return redirect("movies:index")
        else:
            print("Invalid username or passwors")

    # Render login_register page
    context = {"page": page}
    return render(request, "movies/login_register.html", context)


def logoutUser(request):
    # Call user logout function to logout
    logout(request)
    return redirect("movies:index")


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
            return redirect("movies:index")
        else:
            print("Error in registration")

    # Render register form
    return render(request, "movies/login_register.html", {"form": form})


# Movies
def movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {"page_title": "Movie Details", "movie": movie}
    return render(request, "movies/movie.html", context)


def addMovie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)

        if form.is_valid():
            Movie.objects.create(
                name=request.POST.get("name"),
                description=request.POST.get("description"),
                year=request.POST.get("year"),
                rating=request.POST.get("rating"),
                posted_by=request.user,
            )

            return redirect("movies:index")
    else:
        form = MovieForm()

    return render(request, "movies/movie_form.html", {"form": form})


# View to update movie with form
def updateMovie(request, movie_id):
    # Get movie object from db with id by using model
    movie = get_object_or_404(Movie, id=movie_id)
    # Generate Movieform for movie
    form = MovieForm(instance=movie)

    # When form submitted get values
    if request.method == "POST":
        # Update model based on form values
        movie.name = request.POST.get("name")
        movie.description = request.POST.get("description")
        movie.year = request.POST.get("year")
        movie.rating = request.POST.get("rating")
        # Save model in db
        movie.save()
        # Redirect to home
        return redirect("movies:movie", movie_id=movie_id)

    # Return and render movie form
    context = {"form": form, "movie": movie}
    return render(request, "movies/movie_form.html", context)


# Route to delete movie
def deleteMovie(request, movie_id):
    # Get movie object from db using model
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        # Delete movie object and dbs
        movie.delete()
        # Returb home
        return redirect("movies:index")
    # Render confirm delete page
    return render(request, "movies/delete_movie.html", {"obj": movie})


# Reviews


def addReview(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                user=request.user,
                movie=movie,
                review=request.POST.get("review"),
                rating=request.POST.get("rating"),
            )
            return redirect("movies:movie", movie_id=movie_id)
    else:
        form = ReviewForm()
    return render(request, "movies/review_form.html", {"form": form, "movie": movie})


def editReview(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id, movie_id=movie_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("movies:movie", movie_id=movie_id)
    else:
        form = ReviewForm(instance=review)
    return render(
        request, "movies/review_form.html", {"form": form, "movie": review.movie}
    )


def deleteReview(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id, movie_id=movie_id)
    if request.method == "POST":
        review.delete()
        return redirect("movies:movie", movie_id=movie_id)
    return render(request, "movies/delete_review.html", {"review": review})
