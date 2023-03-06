from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAdminOrAccountOwner
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUserView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    lookup_url_kwarg = "user_id"