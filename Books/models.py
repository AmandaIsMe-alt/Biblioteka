from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
