from django.urls import path, include
from rest_framework import routers

from apps.autor.api.viewsets import AuthorViewSet

router = routers.DefaultRouter()

router.register('', AuthorViewSet, basename="autor")

urlpatterns = [
    path('', include(router.urls)),
]