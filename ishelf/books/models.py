import os.path
from django.contrib.auth.models import User
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    ImageField,
    IntegerField,
    Model,
    TextField,
    CASCADE
)
from django.utils.translation import ugettext_lazy as _

BOOKS_MEDIA_PREFIX = 'books'


def book_media_directory(instance, filename):
    if isinstance(instance, Book):
        path = os.path.join(instance.isbn, filename)
    else:
        path = os.path.join(instance.book.isbn, filename)
    return os.path.join(BOOKS_MEDIA_PREFIX, path)


class Author(Model):
    first_name = CharField(max_length=127, verbose_name=_('First name'))
    last_name = CharField(max_length=127, verbose_name=_('Last name'))
    active = BooleanField(default=True, verbose_name=_('Active'))
    created_at = DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return str('{} {}'.format(self.first_name, self.last_name))

    class Meta:
        ordering = ['id']
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Book(Model):
    title = CharField(max_length=255, verbose_name=_('Title'))
    subtitle = CharField(max_length=255, verbose_name=_('Subtitle'))
    published = DateTimeField(verbose_name=_('Published'))
    regular_price = DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Regular price'))
    discount_price = DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Discount price'))
    description = TextField(max_length=1023, verbose_name=_('Description'))
    isbn = CharField(max_length=127, verbose_name=_('ISBN'))
    pages = IntegerField(default=1, verbose_name=_('Pages'))
    active = BooleanField(default=True, verbose_name=_('Active'))
    created_at = DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    author = ForeignKey(Author, verbose_name=_('Author'), on_delete=CASCADE)
    cover = ImageField(upload_to=book_media_directory, blank=True)

    def __str__(self):
        return str('{} - {}'.format(self.title, self.author.__str__()))

    class Meta:
        ordering = ['id']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


class BookBookmark(Model):
    book = ForeignKey(Book, verbose_name=_('Book'), on_delete=CASCADE)
    user = ForeignKey(User, verbose_name=_('User'), on_delete=CASCADE)

    def __str__(self):
        return str('{} - {}'.format(self.book.__str__(), self.user.__str__()))

    class Meta:
        unique_together = (('book', 'user'),)
        ordering = ['id']
        verbose_name = _('Bookmark')
        verbose_name_plural = _('Bookmarks')


class BookRate(Model):
    book = ForeignKey(Book, verbose_name=_('Book'), on_delete=CASCADE)
    user = ForeignKey(User, verbose_name=_('User'), on_delete=CASCADE)
    score = DecimalField(max_digits=2, decimal_places=1, verbose_name=_('score'))

    def __str__(self):
        return str('{} - {} - {}'.format(self.book.__str__(), self.user.__str__(), self.score))

    class Meta:
        unique_together = (('book', 'user'),)
        ordering = ['id']
        verbose_name = _('Score')
        verbose_name_plural = _('Scores')
