from django.shortcuts import render
from .models import Book  # Assuming you have a Book model
from django.shortcuts import render, get_object_or_404
from .models import Library


def list_books(request):
    # Query the database for all books
    books = Book.objects.all()

    # Pass the books to the template
    return render(request, 'relationship_app/list_books.html', {'books': books})

# relationship_app/views.py

def library_detail(request, library_id):
    # Fetch the Library instance or return a 404 if not found
    library = get_object_or_404(Library, id=library_id)
    
    # Render the library_detail.html template with the library context
    return render(request, 'relationship_app/library_detail.html', {'library': library})
