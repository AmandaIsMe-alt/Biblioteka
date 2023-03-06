from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Book
from .serializers import BookSerializer
# Create your views here.


class BookView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    lookup_url_kwarg = "book_id"
