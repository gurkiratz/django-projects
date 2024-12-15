from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.
class Movie(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  year = models.PositiveIntegerField()
  # Attribute to store rating as int, use validators for min and max values
  rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
  # Store user that posed the movie, set null if user deleted
  posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Review(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  review = models.TextField(max_length=100000)
  rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

  def __str__(self):
    return self.movie.name