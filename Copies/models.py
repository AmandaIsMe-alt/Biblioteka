from django.db import models

class Copy(models.Model):
    total_amount =  models.IntegerField()
    borrow_amount = models.IntegerField()
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)

class Borrow(models.Model):
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add=True)
    copy = models.ForeignKey("copies.Copy", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
