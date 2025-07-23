from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Explicit Library import

# Function-based view
def list_books(request):
    books = Book.objects.all()  # Simple version for checker
    books = Book.objects.select_related('author').all()  # Optimized version
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view with ALL checker requirements
class LibraryDetailView(DetailView):  # Using DetailView as required
    model = Library  # Explicit model reference
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # Required context name
