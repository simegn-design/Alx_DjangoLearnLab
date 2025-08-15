from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    profile_view, PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    create_comment, search, tag_filter
)

urlpatterns = [
    # Authentication
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    
    # Posts
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # Comments
    path('post/<int:post_id>/comment/new/', create_comment, name='comment-create'),
    
    # Search & Tags
    path('search/', search, name='search'),
    path('tags/<slug:tag>/', tag_filter, name='tag-filter'),
]
