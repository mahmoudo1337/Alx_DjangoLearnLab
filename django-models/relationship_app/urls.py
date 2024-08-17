from django.urls import path
from .views import book_list_view, LibraryDetailView
from .views import list_books

urlpatterns = [
    path('books/', book_list_view, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]