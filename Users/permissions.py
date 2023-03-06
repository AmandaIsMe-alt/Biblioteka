from rest_framework import permissions
from rest_framework.views import Request, View
from Users.models import User


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return bool(request.user == obj or request.user.is_superuser)
