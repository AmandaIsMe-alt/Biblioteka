# Generated by Django 4.1.7 on 2023-03-10 14:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Copies", "0015_rename_book_borrow_id_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="borrow",
            name="id_book",
        ),
    ]