from rest_framework import serializers
from apps.livro.models import Book
from apps.autor.models import Author
from apps.categoria.models import Category

class BookSerializer(serializers.ModelSerializer):

    authors = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field="name", many=True)
    categories = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field="name", many=True)

    class Meta:
        model = Book
        fields = ["id", "title", "description", "date", "authors", "categories"]