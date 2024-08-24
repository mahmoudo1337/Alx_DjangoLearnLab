from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm

# Create Groups
editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')

# Get Permissions
content_type = ContentType.objects.get_for_model(Book)
can_view = Permission.objects.get(codename='can_view', content_type=content_type)
can_create = Permission.objects.get(codename='can_create', content_type=content_type)
can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

# Assign Permissions to Groups
editors_group.permissions.add(can_create, can_edit)
viewers_group.permissions.add(can_view)
admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    # Logic for creating a book
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'relationship_app/create_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Logic for editing a book
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    # Logic for deleting a book
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')


#books

def search_books(request):
    query = request.GET.get('q')
    results = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'results': results})