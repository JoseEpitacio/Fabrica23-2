from django.urls import path, include
from rest_framework import routers

from apps.categoria.api.viewsets import CategoryViewSet

router = routers.DefaultRouter()

router.register('', CategoryViewSet, basename="categoria")

urlpatterns = [
    path('', include(router.urls)),
]