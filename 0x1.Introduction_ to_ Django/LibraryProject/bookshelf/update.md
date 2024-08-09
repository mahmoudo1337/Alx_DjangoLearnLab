```python
# Update the book title
retrieved_book.title = 'Nineteen Eighty-Four'
retrieved_book.save()

# Verify update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)  # Output: Nineteen Eighty-Four