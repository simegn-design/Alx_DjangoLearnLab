from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

def books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()

def get_librarian(library_name):
    return Librarian.objects.get(library__name=library_name)
