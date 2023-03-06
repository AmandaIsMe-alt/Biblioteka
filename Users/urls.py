from django.urls import path
from .views import CreateUserView, UpdateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("users/<int:user_id>/", UpdateUserView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
