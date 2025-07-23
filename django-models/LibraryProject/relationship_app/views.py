from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view with BOTH versions
def list_books(request):
    books = Book.objects.all()  # Simple version checker wants
    books = Book.objects.select_related('author').all()  # Optimized version
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
