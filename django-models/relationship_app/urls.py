from django.urls import path
from .views import book_list_view, LibraryDetailView
from .views import list_books
from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path('books/', book_list_view, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
]

# views.register