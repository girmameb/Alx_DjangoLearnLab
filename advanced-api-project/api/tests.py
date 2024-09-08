from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create some books
        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2000)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2001)

        # Initialize the API client
        self.client = APIClient()

    def test_create_book_authenticated(self):
        # Authenticate
        self.client.login(username='testuser', password='testpassword')

        # Data to be sent in POST request
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2024
        }

        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2024
        }
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Updated Book'}
        response = self.client.patch(reverse('book-detail', args=[self.book1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        response = self.client.get(reverse('book-list') + '?title=Book%20One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Book One')

    def test_search_books(self):
        response = self.client.get(reverse('book-list') + '?search=Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_order_books(self):
        response = self.client.get(reverse('book-list') + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Book One')
