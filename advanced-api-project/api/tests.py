from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Author

class BookTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "Sample Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
