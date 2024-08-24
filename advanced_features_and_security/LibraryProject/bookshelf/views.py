# advanced_features_and_security/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article

@permission_required('bookshelf.can_view', raise_exception=True)
def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'bookshelf/article_detail.html', {'article': article})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        # Handle form submission
        # Save the new article
        return redirect('article_list')
    return render(request, 'bookshelf/article_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        # Handle form submission
        # Update the article
        return redirect('article_detail', article_id=article.id)
    return render(request, 'bookshelf/article_form.html', {'article': article})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'bookshelf/article_confirm_delete.html', {'article': article})
