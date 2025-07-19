from django.urls import path
from .views import list_books, LibraryDetailView, role_based_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin-view/', role_based_view, {'role': 'Admin'}, name='admin_view'),
]
