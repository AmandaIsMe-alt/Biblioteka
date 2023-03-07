from django.urls import path
from .views import CopyDetailView, CopyView

urlpatterns = [
    path("copies/", CopyView.as_view()),
    path("copies/<int:pet_id>/", CopyDetailView.as_view()),
]