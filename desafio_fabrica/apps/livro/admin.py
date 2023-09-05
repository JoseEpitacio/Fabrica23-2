from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    fields = ["title", "description", "date", "authors", "categories"]