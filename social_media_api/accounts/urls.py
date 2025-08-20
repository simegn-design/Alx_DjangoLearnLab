from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('follow-stats/', views.user_follow_stats, name='follow-stats'),
]
