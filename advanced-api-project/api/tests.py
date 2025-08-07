from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test data
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Sample Book",
            publication_year=2020,
            author=self.author
        )
        
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create authenticated client
        self.auth_client = APIClient()
        self.auth_client.force_authenticate(user=self.user)

    # Unauthenticated tests
    def test_book_list_unauthenticated(self):
        url = reverse('api:book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_book_detail_unauthenticated(self):
        url = reverse('api:book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)

