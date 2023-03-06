from rest_framework import permissions, SAFE_METHODS
from rest_framework.views import Request, View


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_librarian and
            request.user.is_authenticated
        )
