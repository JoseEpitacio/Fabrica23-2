from rest_framework import serializers
from apps.livro.models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "title", "description", "date", "authors"]