# Update Operation

**Command:**

```python
# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Output the updated book
book
