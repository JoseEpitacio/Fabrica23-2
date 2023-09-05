from django.urls import path, include
from rest_framework import routers
from apps.livro.api.viewsets import BookViewSet

from . import views

router = routers.DefaultRouter()

router.register('', BookViewSet, basename="books")

urlpatterns = [
    #path('template', views.pagination, name="pagination"),
    path('', include(router.urls)),
]