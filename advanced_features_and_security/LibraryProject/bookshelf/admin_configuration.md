# Django Admin Configuration for Book Model

## Register the Book Model

In `bookshelf/admin.py`, register the `Book` model with the Django admin:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # List display configuration
    list_display = ('title', 'author', 'publication_year')
    
    # Search fields configuration
    search_fields = ('title', 'author')
    
    # List filter configuration
    list_filter = ('publication_year',)
