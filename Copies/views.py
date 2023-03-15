from .models import Copy, Borrow
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CopySerializer, BorrowSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics
from Copies.models import Borrow
from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.exceptions import APIException
from Users.models import User
import pytz
from rest_framework.response import Response
from Books.models import Book, Follow
from django.core.mail import send_mail
from django.conf import settings


class UserHadPendencys(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class CopyView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyDetailView(generics.CreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        found_book = Book.objects.filter(id=self.kwargs.get("book_id"))

        if not found_book:
            raise UserHadPendencys("There is no book with that ID")

        serializer.save(book_id=self.kwargs.get("book_id"))


class BorrowView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = BorrowSerializer

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user.id)


class BorrowDetailView(generics.CreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def perform_create(self, serializer):
        user = User.objects.filter(pk=self.kwargs.get("user_id")).first()
        days = datetime.now(pytz.UTC)

        if not user:
            raise UserHadPendencys("User does not exist")

        if user.blocked_until:
            if user.blocked_until > days:
                raise UserHadPendencys("User is blocked", 400)

        user_borrows = Borrow.objects.filter(user_id=self.kwargs.get("user_id"))
        if user_borrows:
            for borrow in user_borrows:
                if borrow.returned is False:
                    date = borrow.return_date
                    is_before = date - days
                    if is_before.total_seconds() < 0:
                        block_time = days + timedelta(days=7)
                        user.blocked_until = block_time
                        user.save()
                        raise UserHadPendencys("User is blocked")

        serializer.save(
            user_id=self.kwargs.get("user_id"),
            copy_id=self.kwargs.get("copie_id"),
        )


class BorrowReturn(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    lookup_field = "copie_id"

    def patch(self, request, *args, **kwargs):
        borrow = Borrow.objects.filter(
            user_id=self.kwargs.get("user_id"),
            copy=self.kwargs.get("copie_id"),
            returned=False,
        ).first()

        days = datetime.now(pytz.UTC)

        if not borrow:
            return Response({"error": "Borrow not found"}, status=404)

        if borrow.return_date < days:
            user = User.objects.filter(pk=self.kwargs.get("user_id")).first()
            block_time = days + timedelta(days=7)
            user.blocked_until = block_time
            user.save()
            borrow.returned = True
            borrow.save()
            return Response(
                {
                    "message": "You were late returning the book so you were blocked from making new borrows for 7 days"
                },
                status=200,
            )

        copy1 = Copy.objects.filter(id=self.kwargs.get("copie_id")).first()
        copy1.is_active = True
        copy1.save()

        book = Book.objects.filter(id=copy1.book_id).first()

        borrow.returned = True
        borrow.save()

        verified_copies = Copy.objects.filter(is_active=True).all()

        follow = Follow.objects.filter(book=copy1.book_id).first()

        if follow:
            if verified_copies.count() > 0:
                follows = Follow.objects.filter(book=copy1.book_id).all()

                emails = [follow.user.email for follow in follows]

                send_mail(
                    subject="O livro que você segue está disponível na BiblioteKA",
                    message="O livro que você segue está disponível na BiblioteKA.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=emails,
                    fail_silently=False,
                )

        return Response({"success": "Book successfully returned"}, status=200)
