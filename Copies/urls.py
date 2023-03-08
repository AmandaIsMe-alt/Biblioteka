from django.urls import path
from .views import CopyView, CopyDetailView

urlpatterns = [
    path("copies/", CopyView.as_view()),
    path("copies/<int:copie_id>/", CopyDetailView.as_view()),
]