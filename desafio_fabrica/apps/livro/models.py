from django.db import models
from apps.autor.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    authors = models.ManyToManyField(Author, related_name="books", blank=True)

    def __str__(self):
        return self.title