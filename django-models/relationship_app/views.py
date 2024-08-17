from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import login

# Create your views here.

def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'library'


class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view (using built-in LogoutView)
class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view (using generic CreateView and built-in UserCreationForm)
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')