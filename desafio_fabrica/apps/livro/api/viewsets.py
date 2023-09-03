from rest_framework.viewsets import ModelViewSet

from apps.livro.models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer