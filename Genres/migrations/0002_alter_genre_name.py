# Generated by Django 4.1.7 on 2023-03-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
