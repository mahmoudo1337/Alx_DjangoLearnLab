from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve a specific book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.permissions import IsAuthenticated

# Create a new book
class BookCreateView(generics.CreateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [IsAuthenticated]

   # You can override the `perform_create` method to modify behavior
   def perform_create(self, serializer):
       serializer.save()  # Save the book instance


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [IsAuthenticated]

   # You can override the `perform_update` method to add custom logic
   def perform_update(self, serializer):
       serializer.save()  # Update the book instance
# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

from rest_framework.permissions import AllowAny

class BookListView(generics.ListAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [AllowAny]  # Publicly accessible

class BookDetailView(generics.RetrieveAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [AllowAny]  # Publicly accessible

class BookCreateView(generics.CreateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [IsAuthenticated]  # Only authenticated users can create

class BookUpdateView(generics.UpdateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [IsAuthenticated]  # Only authenticated users can update

class BookDeleteView(generics.DestroyAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [IsAuthenticated]  # Only authenticated users can delete
