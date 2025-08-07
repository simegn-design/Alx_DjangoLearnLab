from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),  # Exact match
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # Exact match
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
]
