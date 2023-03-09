# Generated by Django 4.1.7 on 2023-03-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_blocked",
        ),
        migrations.AddField(
            model_name="user",
            name="blocked_until",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
