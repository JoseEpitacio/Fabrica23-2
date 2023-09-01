from django.urls import path, include
from rest_framework import routers

from apps.todo.api.viewsets import TaskViewSet

# Criação da endpoint
router = routers.DefaultRouter()

router.register("", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls)),
]
