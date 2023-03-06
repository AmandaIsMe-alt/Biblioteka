from django.urls import path
from .views import BookView, BookDetailView

urlpatterns = [
    path("book/", BookView.as_view()),
    path("book/<int:book_id>/", BookDetailView.as_view()),
]