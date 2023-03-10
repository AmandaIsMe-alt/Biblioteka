from django.db import models
from Users.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    synopsis = models.TextField(null=True)
    publisher_company = models.CharField(max_length=255, default="Freelancer Work")

    genres = models.ManyToManyField('Genres.Genre', related_name="books")
    
    follows = models.ManyToManyField(
        User,
        through="Books.Follow",
        related_name="user_follows",
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_follow",
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="books_follow",
    )
