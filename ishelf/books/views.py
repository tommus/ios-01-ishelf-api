from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)

from rest_framework.viewsets import GenericViewSet

from ishelf.books.models import (
    Author,
    Book,
    BookBookmark,
    BookRate,
)

from ishelf.books.serializers import (
    AuthorSerializer,
    BookSerializer,
    BookBookmarkSerializer,
    BookRateSerializer,
)


class AuthorViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                    GenericViewSet):
    filter_fields = ['active']
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                  GenericViewSet):
    filter_fields = ['active']
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookBookmarkViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                          GenericViewSet):
    filter_fields = ['active']
    queryset = BookBookmark.objects.all()
    serializer_class = BookBookmarkSerializer


class BookRateViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                      GenericViewSet):
    filter_fields = ['active']
    queryset = BookRate.objects.all()
    serializer_class = BookRateSerializer
