# relationship_app/views.py

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
