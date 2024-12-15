from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books", null=True
    )

    def __str__(self):
        return self.title
