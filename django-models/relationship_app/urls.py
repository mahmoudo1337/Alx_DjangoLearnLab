from django.urls import path
from .views import book_list_view, LibraryDetailView
from .views import list_books
from .views import LoginView, LogoutView, RegisterView
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', book_list_view, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('admin-dashboard/', admin_view, name='admin-view'),
    path('librarian-dashboard/', librarian_view, name='librarian-view'),
    path('member-dashboard/', member_view, name='member-view'),
    path('add/', add_book, name='add-book'),
    path('edit/<int:book_id>/', edit_book, name='edit-book'),
    path('delete/<int:book_id>/', delete_book, name='delete-book'),
]

# views.register