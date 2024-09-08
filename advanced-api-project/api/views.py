from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import Book
from .serializers import BookSerializer

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    publication_year = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookListView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    - GET: Retrieve a list of books with optional filtering, searching, and ordering.
    - POST: Create a new book (authenticated users only).

    Filtering:
    - Filter by title: ?title=Some%20Title
    - Filter by author: ?author=Some%20Author
    - Filter by publication year: ?publication_year=2023

    Searching:
    - Search in title and author fields: ?search=Some%20Text

    Ordering:
    - Order by title: ?ordering=title
    - Order by publication year: ?ordering=publication_year
    - Descending order: prepend the field name with a minus sign (e.g., -title)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific book.
    - GET: Retrieve a book by ID (public access).
    - PUT/PATCH: Update a book by ID (authenticated users only).
    - DELETE: Delete a book by ID (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
