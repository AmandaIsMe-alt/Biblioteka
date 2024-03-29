# Generated by Django 4.1.7 on 2023-03-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genres', '0002_alter_genre_name'),
        ('Books', '0003_remove_book_genre_book_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='books', to='Genres.genre'),
        ),
    ]
