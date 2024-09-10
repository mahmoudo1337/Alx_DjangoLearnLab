from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Author, Book
from .serializers import BookSerializer


class BookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='John Doe')
        self.book_data = {
            'title': 'Sample Book',
            'publication_year': 2021,
            'author': self.author.id
        }
    
    def test_create_book(self):
        response = self.client.post(reverse('book-list'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])


    def test_list_books(self):
        Book.objects.create(title='Book 1', publication_year=2021, author=self.author)
        Book.objects.create(title='Book 2', publication_year=2020, author=self.author)

        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
    def test_update_book(self):
        book = Book.objects.create(title='Book 1', publication_year=2021, author=self.author)
        updated_data = {'title': 'Updated Book', 'publication_year': 2022, 'author': self.author.id}

        response = self.client.put(reverse('book-detail', kwargs={'pk': book.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])

    def test_update_book(self):
        book = Book.objects.create(title='Book 1', publication_year=2021, author=self.author)
        updated_data = {'title': 'Updated Book', 'publication_year': 2022, 'author': self.author.id}

        response = self.client.put(reverse('book-detail', kwargs={'pk': book.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])
    def test_delete_book(self):
        book = Book.objects.create(title='Book 1', publication_year=2021, author=self.author)

        response = self.client.delete(reverse('book-detail', kwargs={'pk': book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    def test_filter_books_by_publication_year(self):
        Book.objects.create(title='Book 1', publication_year=2021, author=self.author)
        Book.objects.create(title='Book 2', publication_year=2020, author=self.author)

        response = self.client.get(reverse('book-list'), {'publication_year': 2021})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')
    def test_search_books_by_title(self):
        Book.objects.create(title='Book 1', publication_year=2021, author=self.author)
        Book.objects.create(title='Another Book', publication_year=2020, author=self.author)

        response = self.client.get(reverse('book-list'), {'search': 'Another'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Another Book')
    def test_order_books_by_title(self):
        Book.objects.create(title='Book B', publication_year=2021, author=self.author)
        Book.objects.create(title='Book A', publication_year=2020, author=self.author)

        response = self.client.get(reverse('book-list'), {'ordering': 'title'})
        self.assertEqual(response.data[0]['title'], 'Book A')
from rest_framework.test import APIClient

class AuthenticatedBookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='John Doe')
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    def test_create_book_requires_auth(self):
        self.client.force_authenticate(user=self.user)
        book_data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}

        response = self.client.post(reverse('book-list'), book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
