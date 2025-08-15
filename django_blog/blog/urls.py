from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    PostListView, PostDetailView, 
    PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Authentication URLs (Task 1)
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # CRUD URLs (Task 2)
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
