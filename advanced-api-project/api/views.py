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

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
   filterset_fields = ['title', 'author__name', 'publication_year']  # Filter by these fields
   search_fields = ['title', 'author__name']  # Search by title or author’s name
   ordering_fields = ['title', 'publication_year']  # Order by title or publication year
   ordering = ['title']  # Default ordering by title


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


