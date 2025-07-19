from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Library, UserProfile

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

@login_required
def role_based_view(request, role):
    profile = UserProfile.objects.get(user=request.user)
    if profile.role == role:
        return render(request, f'relationship_app/{role}_view.html')
    return HttpResponseForbidden()
