# advanced_features_and_security/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_article(request, article_id):
    article = get_object_or_404(Book, id=article_id)
    return render(request, 'bookshelf/Book_detail.html', {'article': article})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        # Handle form submission
        # Save the new article
        return redirect('Book_list')
    return render(request, 'bookshelf/Book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, book_id):
    article = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle form submission
        # Update the article
        return redirect('book_detail', book_id = Book.id)
    return render(request, 'bookshelf/article_form.html', {'article': article})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Book, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': article})
