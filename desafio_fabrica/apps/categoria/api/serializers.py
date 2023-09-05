from rest_framework import serializers
from apps.categoria.models import Category
from apps.livro.models import Book

class CategorySerializer(serializers.ModelSerializer):

    books = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field="title", many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "books"]