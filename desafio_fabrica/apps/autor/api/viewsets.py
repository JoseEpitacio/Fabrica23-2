from rest_framework.viewsets import ModelViewSet

from apps.autor.models import Author
from .serializers import AuthorSerializer

from rest_framework.pagination import LimitOffsetPagination

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = LimitOffsetPagination