from django.db import models

# Create your models here.

# model for create a new movie
class MovieDetails(models.Model):
    movie_name = models.CharField(max_length=250)
    movie_description = models.TextField()
    release_date = models.DateField()
    movie_duration = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return f"{self.movie_name}"
    