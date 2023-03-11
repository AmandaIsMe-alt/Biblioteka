from django.urls import path
from .views import CopyView, CopyDetailView, BorrowView, BorrowReturn

urlpatterns = [
    path("copies/", CopyView.as_view()),
    path("copies/<int:book_id>/", CopyDetailView.as_view()),
    path("borrow/<int:copie_id>/<int:user_id>/", BorrowView.as_view()),
    path("borrow/return/<int:copie_id>/<int:user_id>/", BorrowReturn.as_view()),
]
