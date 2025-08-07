from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def validate_publication_year(self, value):
        from datetime import datetime
        if value > datetime.now().year:
            raise serializers.ValidationError("Year cannot be future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
