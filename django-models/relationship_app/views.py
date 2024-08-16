from django.shortcuts import render
from .models import Book  # Assuming you have a Book model

def list_books(request):
    # Query the database for all books
    books = Book.objects.all()

    # Pass the books to the template
    return render(request, 'relationship_app/list_books.html', {'books': books})
