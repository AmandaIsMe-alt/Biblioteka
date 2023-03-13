from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Book, Follow
from .serializers import BookSerializer, FollowSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
from django.shortcuts import get_object_or_404

# Create your views here.


class AlreadyFollow(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class BookView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_url_kwarg = "book_id"


class FollowView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        book_found = Book.objects.filter(id=self.kwargs.get("book_id"))

        already_follow = Follow.objects.filter(
            book_id=self.kwargs.get("book_id"), user=self.request.user
        )
<<<<<<< HEAD
        if not book_found:
            raise AlreadyFollow("This book does not exist")
        elif already_follow:
=======
        
        if already_follow:
>>>>>>> cc38fe2986de628ea7395c390e26185c6f62dbce
            raise AlreadyFollow("Already following this book")
        
        book = get_object_or_404(Book, pk=self.kwargs.get("book_id"))

        serializer.save(book=book, user=self.request.user)
