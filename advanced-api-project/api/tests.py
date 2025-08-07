from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Sample Book",
            publication_year=2020,
            author=self.author
        )

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_book_filter(self):
        url = reverse('book-list') + '?title__contains=Sample'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_book_create_auth(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)  # Unauthorized
