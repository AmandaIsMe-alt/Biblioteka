from django.db import models


class Copy(models.Model):
    is_active = models.BooleanField(default=True)

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
    returned = models.BooleanField(default=False)

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
