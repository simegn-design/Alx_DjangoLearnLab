from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

urlpatterns += [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), 
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('register/', CreateView.as_view(
        template_name='relationship_app/register.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('login')
    )),
]
from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
from .views import add_book, edit_book, delete_book

urlpatterns += [
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:pk>/', edit_book, name='edit_book'),
    path('delete-book/<int:pk>/', delete_book, name='delete_book'),
]
