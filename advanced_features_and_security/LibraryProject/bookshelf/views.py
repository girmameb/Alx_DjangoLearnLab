# advanced_features_and_security/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.db.models import Q
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
from .forms import ExampleForm
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/form_example.html', {'form': form})
@permission_required('bookshelf.can_delete', raise_exception=True)


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})


def search_books(request):
    query = request.GET.get('q', '')
    # Safe query using Django ORM
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})

class CSPMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = "default-src 'self';"
        return response

    def add_book(request):
        if request.method == 'POST':
            form = ExampleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_list')
        else:
            form = ExampleForm()
        return render(request, 'bookshelf/form_example.html', {'form': form})

    def book_list(self, request):
        books = Book.objects.all()
        return render(request, 'bookshelf/book_list.html', {'books': books})