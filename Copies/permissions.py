from rest_framework import permissions
from rest_framework.views import Request, View
from workalendar.america import Brazil
import datetime


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.user.is_authenticated and request.user.is_librarian:
            return True

        else:
            return False
    

