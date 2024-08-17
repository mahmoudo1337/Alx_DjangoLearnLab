from django.urls import path
from .views import book_list_view, LibraryDetailView
from .views import list_books
from .views import UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    path('books/', book_list_view, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]