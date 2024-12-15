# Import ModelForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# Import movie
from .models import Movie, Review

# Create movie form
class MovieForm(ModelForm):
  class Meta:
    model = Movie
    fields = '__all__'
    exclude = ['posted_by', 'updated_at', 'created_at']

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['review', 'rating']