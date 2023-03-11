from rest_framework import permissions


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.user.is_authenticated and request.user.is_librarian:
            return True

        else:
            return False


class IsAdminOrReadAccountOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, borrows):
        if request.user.is_librarian:
            return True
        
        for borrow in borrows:
            if borrow.user.id != request.user.id:
                return False
        
        return True