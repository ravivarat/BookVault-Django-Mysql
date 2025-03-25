from django.contrib import admin
from .models import Admin, Book

# Register Admin model
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('email',)  # Display admin emails
    search_fields = ('email',)

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'available')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('available', 'published_date')
