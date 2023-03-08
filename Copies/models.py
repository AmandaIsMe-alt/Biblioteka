from django.db import models
from Users.models import User


class Copy(models.Model):
    total_amount = models.IntegerField(null=True, default=50)
    borrow_amount = models.IntegerField(null=True, default=0)
    teste = models.CharField(max_length=50, null=True)

    book = models.ForeignKey(
        "Books.Book",
        on_delete=models.CASCADE,
        related_name="book_copy",
    )

    borrows = models.ManyToManyField(
        "Users.User",
        through="Copies.Borrow",
        related_name="user_borrows",
    )


class Borrow(models.Model):
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    copy = models.ForeignKey(
        "Copies.Copy",
        on_delete=models.CASCADE,
        related_name="copy_borrow",
    )
    user = models.ForeignKey(
        "Users.User",
        on_delete=models.CASCADE,
        related_name="user_borrow",
    )
