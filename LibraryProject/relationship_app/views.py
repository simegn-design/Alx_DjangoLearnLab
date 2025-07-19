from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def role_check(user, role):
    return UserProfile.objects.get(user=user).role == role

@user_passes_test(lambda u: role_check(u, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: role_check(u, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: role_check(u, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    return render(request, 'relationship_app/delete_book.html')
