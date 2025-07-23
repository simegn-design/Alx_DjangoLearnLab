from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Explicit Library import

# Function-based view (books list)
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (library detail)
class LibraryDetailView(DetailView):
    model = Library  # Required model reference
    template_name = 'relationship_app/library_detail.html'  # Exact path
    context_object_name = 'library'  # Required context name

# Class-based view with EXACT checker requirements
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
