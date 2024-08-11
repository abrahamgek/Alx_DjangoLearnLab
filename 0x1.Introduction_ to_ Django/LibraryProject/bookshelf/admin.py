from django.contrib import admin

# Register your models here.

from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for the list view
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')

# Register the Book model with the custom admin interface
admin.site.register(Book, BookAdmin)