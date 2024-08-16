from .models import Book
from django.contrib import admin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # List display configuration
    list_display = ('title', 'author', 'publication_year')
    
    # Search fields configuration
    search_fields = ('title', 'author')
    
    # List filter configuration
    list_filter = ('publication_year',)

