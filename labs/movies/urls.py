from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    # auth urls
    path('login/', views.loginPage, name="login"),
    # Route for login page
    path('logout/', views.logoutUser, name="logout"),
    # Route for register page
    path('register/', views.registerUser, name="register"),

    # movie urls
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.movie, name='movie'),
    path('add_movie/', views.addMovie, name="add_movie"),
    path('<int:movie_id>/update_movie/', views.updateMovie, name='update_movie'),
    path('<int:movie_id>/delete_movie/', views.deleteMovie, name='delete_movie'),

    # review urls
    path('<int:movie_id>/add_review/', views.addReview, name='add_review'),
    path('<int:movie_id>/edit_review/<int:review_id>/', views.editReview, name='edit_review'),
    path('<int:movie_id>/delete_review/<int:review_id>/', views.deleteReview, name='delete_review'),
]
