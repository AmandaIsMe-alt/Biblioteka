# Generated by Django 4.1.7 on 2023-03-09 16:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Copies", "0009_alter_borrow_return_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="copy",
            name="teste",
        ),
    ]
