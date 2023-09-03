from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.livro.urls')),
    path('autores/', include('apps.autor.urls'))
]
