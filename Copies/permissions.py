from rest_framework import permissions
from datetime import datetime, timedelta
import ipdb


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.user.is_authenticated and request.user.is_librarian:
            return True

        else:
            return False


class BlockedBorrow(permissions.BasePermission):
    def has_permission(self, request, view):
        find_return_date = request.user.user_borrow.all()
        date_now = datetime.now()
        for date in find_return_date:
            if date_now < date.return_date:
                print("NÃO TENHO TEMPO")
            else:
                print("TENHO TEMPO")

        # print("OOOOIIII", teste.borrow_date)
        return True
