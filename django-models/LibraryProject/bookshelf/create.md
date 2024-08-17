```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)

# Verify creation
print(book)  # Output: <Book: 1984>