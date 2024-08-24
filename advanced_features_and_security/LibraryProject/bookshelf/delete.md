### Delete Operation

```python
from bookshelf.models import Book
# Delete the book
retrieved_book.delete()

# Verify deletion
books = Book.objects.all()
print(books.count())  # Output: 0