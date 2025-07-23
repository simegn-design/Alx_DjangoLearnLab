from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.PositiveIntegerField()
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    def __str__(self): return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self): return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self): return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [('Admin','Admin'), ('Librarian','Librarian'), ('Member','Member')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

# Create query_samples.py in same directory
cat > LibraryProject/relationship_app/query_samples.py <<'EOF'
from .models import Author, Book, Library

# Query all books by a specific author
def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# List all books in a library
def books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()

# Retrieve librarian for a library
def get_librarian(library_name):
    return Librarian.objects.get(library__name=library_name)
