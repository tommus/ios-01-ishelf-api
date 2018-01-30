from django.contrib.admin import (
    ModelAdmin,
    register
)

from ishelf.books.models import (
    Author,
    Book,
    BookBookmark,
    BookRate
)


@register(Author)
class AuthorAdmin(ModelAdmin):
    list_filter = ['active']
    list_display = ['__str__', 'active']
    list_editable = ['active']


@register(Book)
class BookAdmin(ModelAdmin):
    list_filter = ['author', 'active']
    list_display = ['__str__', 'active']
    list_editable = ['active']


@register(BookBookmark)
class BookBookmarkAdmin(ModelAdmin):
    pass


@register(BookRate)
class BookRateAdmin(ModelAdmin):
    pass
