from rest_framework.viewsets import ModelViewSet

from apps.autor.models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer