from rest_framework import serializers
from .models import Book

class BookSerializer(generics.ListAPIView):
    class Meta:
        model = Book
        fields = '__all__'