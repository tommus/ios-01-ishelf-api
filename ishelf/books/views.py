from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet

from ishelf.books.models import (
    Author,
    Book,
)
from ishelf.books.serializers import (
    AuthorSerializer,
    BookSerializer,
)


class AuthorViewSet(ModelViewSet):
    """
    list:
    List authors.

    retrieve:
    Retrieve an author details.

    create:
    Create an author.

    update:
    Update an author.

    partial_update:
    Partially update an author.

    destroy:
    Remove an author.
    """
    permission_classes = (IsAuthenticated,)
    filter_fields = ("active",)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    """
    list:
    List books.

    retrieve:
    Retrieve book details.

    create:
    Create a book.

    update:
    Update a book.

    partial_update:
    Partially update a book.

    destroy:
    Remove a book.
    """
    filter_fields = ("active",)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
