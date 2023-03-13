from .models import Copy, Borrow
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CopySerializer, BorrowSerializer
from .permissions import IsAdminOrAccountOwner
from rest_framework import generics



class CopyView(generics.ListCreateAPIView):

    queryset = Copy.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]
    serializer_class = CopySerializer


class CopyDetailView(generics.CreateAPIView):
    queryset = Copy.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        serializer.save(book_id=self.kwargs.get('copie_id'))


class BorrowView(generics.ListCreateAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]

    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.kwargs.get('user_id'), copy_id=self.kwargs.get('copie_id'))

