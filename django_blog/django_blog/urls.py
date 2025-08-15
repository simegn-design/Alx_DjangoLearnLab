from django.contrib import admin
from django.urls import path, include  # <-- Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Includes all blog app URLs
]
