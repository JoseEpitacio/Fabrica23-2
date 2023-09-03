from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
# Create your views here.
def pagination(request):
    livro_list = Book.objects.all()
    book_paginator = Paginator(livro_list, 5)

    page = request.GET.get('page')
    livros = book_paginator.get_page(page)

    return render(request, 'pagination.html', {'livros':livros})