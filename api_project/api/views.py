# from rest_framework.generics import ListAPIView
# from .models import Book
# from .serializers import BookSerializer

# class BookList(generics.ListAPIView ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
