from .models import Copy
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CopySerializer
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
