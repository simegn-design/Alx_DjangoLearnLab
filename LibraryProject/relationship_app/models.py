from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Fixed length
    def __str__(self): return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.PositiveIntegerField()

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):  # Fixed typo (was Libraries)
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # Fixed spelling
