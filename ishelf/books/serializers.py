from rest_framework.serializers import ModelSerializer

from ishelf.books.models import (
    Author,
    Book,
    BookBookmark,
    BookRate
)


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookBookmarkSerializer(ModelSerializer):
    class Meta:
        model = BookBookmark
        fields = '__all__'


class BookRateSerializer(ModelSerializer):
    class Meta:
        model = BookRate
        fields = '__all__'
