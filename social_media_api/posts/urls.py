from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', views.like_post, name='post-like'),
    path('posts/<int:pk>/unlike/', views.unlike_post, name='post-unlike'),
]
