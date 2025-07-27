from django.urls import path
from .views import (
    book_list, 
    LibraryDetailView,
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    # Existing URLs
    path('books/', book_list, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    
    # Auth URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
