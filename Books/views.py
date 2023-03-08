from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Book, Follow
from .serializers import BookSerializer, FollowSerializer
from Users.permissions import IsAdminOrAccountOwner
# Create your views here.


class BookView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAdminOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    lookup_url_kwarg = "book_id"

class FollowView(CreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    

    def perform_create(self, serializer):
        serializer.save(book_id=self.kwargs.get('book_id'), user=self.request.user)
