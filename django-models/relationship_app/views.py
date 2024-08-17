from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

def book_list_view(request):
    books = Book.objects.all()
    book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(f"Books in the library:\n{book_list}")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'library'
    