from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Book, Follow
from .serializers import BookSerializer, FollowSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
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

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    

    def perform_create(self, serializer):
        already_follow = Follow.objects.filter(book_id=self.kwargs.get('book_id'), user=self.request.user)

        if already_follow:
            raise AlreadyFollow("Already following this book")

        serializer.save(book_id=self.kwargs.get('book_id'), user=self.request.user)
