# from rest_framework.generics import ListAPIView
# from .models import Book
# from .serializers import BookSerializer

# class BookList(generics.ListAPIView ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
