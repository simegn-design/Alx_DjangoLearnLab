from django.urls import path
from .views import (
    register_view, login_view, logout_view, profile_view,
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, search,
    PostByTagListView,  # NEW IMPORT
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # Auth (Task 1 - working)
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # Posts (Task 2 - working)
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments (Task 3 - working)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Task 4: Search & Tags (FIXED)
    path('search/', search, name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tag-filter'),  # EXACT MATCH
]
