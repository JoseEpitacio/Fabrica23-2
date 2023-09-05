from rest_framework.viewsets import ModelViewSet

from apps.categoria.models import Category
from .serializers import CategorySerializer

from rest_framework.pagination import LimitOffsetPagination

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination