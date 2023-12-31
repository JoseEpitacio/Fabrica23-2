# Generated by Django 4.2.4 on 2023-09-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0002_remove_category_books'),
        ('livro', '0003_rename_name_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='books', to='categoria.category'),
        ),
    ]
