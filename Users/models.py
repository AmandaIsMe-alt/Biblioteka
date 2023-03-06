from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, error_messages={"unique": "Username already in use"})
    email = models.EmailField(max_length=127, unique=True, error_messages={"unique": "E-mail already in use"})
    password = models.CharField(max_length=127)
    is_librarian = models.BooleanField()
    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)