from django.urls import path
from .views import CopyView, CopyDetailView, BorrowView

urlpatterns = [
    path("copies/", CopyView.as_view()),
    path("copies/<int:copie_id>/", CopyDetailView.as_view()),
    path("borrow/<int:copie_id>/<int:user_id>/", BorrowView.as_view())
]