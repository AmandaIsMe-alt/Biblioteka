# Generated by Django 4.1.7 on 2023-03-07 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Copies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Borrow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("borrow_date", models.DateTimeField(auto_now_add=True)),
                ("return_date", models.DateTimeField(auto_now_add=True)),
                (
                    "copy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="copy_borrow",
                        to="Copies.copy",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_borrow",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="copy",
            name="borrows",
            field=models.ManyToManyField(
                related_name="user_borrows",
                through="Copies.Borrow",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
