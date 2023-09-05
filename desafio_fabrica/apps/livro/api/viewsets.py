from rest_framework.viewsets import ModelViewSet

from apps.livro.models import Book
from apps.categoria.models import Category
from .serializers import BookSerializer

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        requisicao = self.request.query_params.get("categoria")

        if requisicao:
            if Category.objects.get(name = requisicao):
                return Book.objects.filter(categories = Category.objects.get(name = requisicao))
            else:
                return Response("Tem esse não")

        return Book.objects.all()
