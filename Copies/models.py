from django.db import models

class Copy(models.Model):
    total_amount =  models.DateTimeField(auto_now_add=True)
    borrow_amount =  models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey("books.Book", on_delete=models.PROTECT, related_name="Copy")

