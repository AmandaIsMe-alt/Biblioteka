from django.db import models

class GenreChoices(models.TextChoices):
    NOVEL = 'Novel'
    TEXTBOOK = 'Textbook'
    MANUAL = 'Manual'
    ENCYCLOPEDIA = 'Encyclopedia'
    COOK_BOOK = 'Cook book'
    GUIDEBOOK = 'Guidebook'
    BIOGRAPHY = 'Biography'
    AUTOBIOGRAPHY = 'Autobiography'
    SELF_HELP_BOOK = 'Self-help book'
    DICTIONARY = "Dictionary"
    STORYBOOK = 'Storybook'
    GRADED_READER = 'Graded Reader'
    E_BOOK = 'E-book'

# Novel: romance

# Textbook : livro didático

# Manual : manual de instruções

# Encyclopedia : enciclopédia

# Cook book : livro de culinária / receitas

# Guidebook : guia de viagem para turistas

# Biography : biografia

# Autobiography : autobiografia

# Self-help Book : livro de auto-ajuda

# Dictionary : dicionário

# Storybook : livro com uma ou mais histórias para crianças

# Graded Reader : livro com diferentes níveis de dificuldade para quem está estudando uma língua estrangeira

# E-book : livro publicado na Internet


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255, choices=GenreChoices.choices, default=GenreChoices.TEXTBOOK)

