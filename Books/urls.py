from django.urls import path
from .views import BookView, BookDetailView, FollowView

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:book_id>/", BookDetailView.as_view()),
    path("follow/<int:book_id>/", FollowView.as_view()),
]