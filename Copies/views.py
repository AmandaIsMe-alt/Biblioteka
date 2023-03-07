from .models import Copy
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CopySerializer
from .permissions import IsAdminOrAccountOwner
from rest_framework.views import APIView, Response, status
from rest_framework.pagination import PageNumberPagination

class CopyView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]
    serializer_class = [CopySerializer]
    

    def get(self, request):
        copy_list = Copy.objects.all()
        result = self.paginate_queryset(copy_list, request, self)
        serializer = CopySerializer(result, many=True)
        return self.get_paginated_response(serializer.data)



class CopyDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]
    serializer_class = [CopySerializer]
    copy_list = Copy.objects.all()  

    lookup_url_kwarg = "copy_id"