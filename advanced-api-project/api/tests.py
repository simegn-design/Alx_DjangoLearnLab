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

    def test_all_endpoints(self):
        endpoints = [
            ('book-list', None, 200),
            ('book-create', None, 201),  # POST request
            ('book-detail', {'pk': self.book.pk}, 200),
            ('author-list', None, 200),
        ]
        
        for endpoint, kwargs, expected_code in endpoints:
            with self.subTest(endpoint=endpoint):
                url = reverse(f'api:{endpoint}', kwargs=kwargs) if kwargs else reverse(f'api:{endpoint}')
                if endpoint == 'book-create':
                    data = {
                        'title': 'New Book',
                        'publication_year': 2023,
                        'author': self.author.id
                    }
                    response = self.client.post(url, data)
                else:
                    response = self.client.get(url)
                self.assertEqual(response.status_code, expected_code)
