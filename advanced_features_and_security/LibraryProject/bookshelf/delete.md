from bookshelf.models import Book
# Delete Operation

**Command:**

```python
# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
