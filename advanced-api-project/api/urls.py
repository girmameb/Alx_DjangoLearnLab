
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books and create a new one
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, update, or delete a specific book
]

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books and create a new one
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Explicit create URL
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, update, or delete a specific book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Explicit update URL
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Explicit delete URL
]
