from rest_framework.serializers import ModelSerializer

from ishelf.books.models import (
    Author,
    Book,
)


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "active", "created_at", "updated_at",)


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id", "title", "subtitle", "published", "regular_price", "discount_price", "description", "isbn", "pages",
            "active", "created_at", "updated_at", "author", "cover")
