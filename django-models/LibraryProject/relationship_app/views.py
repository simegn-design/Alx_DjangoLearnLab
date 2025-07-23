from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.contrib.auth import login, authenticate  # EXACT imports
from django.contrib.auth.forms import UserCreationForm  # EXACT import
from django.urls import reverse_lazy
from .models import Book, Library

# Existing book views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

# AUTHENTICATION VIEWS (NEW)
def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)  # EXACT match
            return redirect('list_books')
    return render(request, 'relationship_app/login.html')

def user_logout(request):
    logout(request)  # EXACT match
    return redirect('login')

class SignUpView(CreateView):
    form_class = UserCreationForm  # EXACT match
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # EXACT match
        return response
