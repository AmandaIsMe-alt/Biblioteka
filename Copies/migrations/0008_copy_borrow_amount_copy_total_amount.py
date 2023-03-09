# Generated by Django 4.1.7 on 2023-03-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Copies', '0007_copy_teste'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='borrow_amount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='copy',
            name='total_amount',
            field=models.IntegerField(default=50, null=True),
        ),
    ]