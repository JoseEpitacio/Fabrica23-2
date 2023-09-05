from django.db import models
from apps.autor.models import Author
from apps.categoria.models import Category

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    authors = models.ManyToManyField(Author, related_name="books", blank=True)
    categories = models.ManyToManyField(Category, related_name="books")

    def __str__(self):
        return self.title