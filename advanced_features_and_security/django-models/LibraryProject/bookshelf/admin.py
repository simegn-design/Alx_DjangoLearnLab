from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

# Task 0: Custom User Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Task 1: Book permissions in admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('library',)
    search_fields = ('title', 'author')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
