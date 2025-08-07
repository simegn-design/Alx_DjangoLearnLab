from django_filters import rest_framework as filters
from rest_framework import generics, permissions, filters as drf_filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'contains'],
            'author__name': ['exact'],
            'publication_year': ['exact', 'gte', 'lte']
        }

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
        drf_filters.OrderingFilter
    ]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        # Get book ID from request data instead of URL
        book_id = self.request.data.get('id')
        return Book.objects.get(id=book_id)

class BookDeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        # Get book ID from request data instead of URL
        book_id = self.request.data.get('id')
        return Book.objects.get(id=book_id)

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
