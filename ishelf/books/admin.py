from django.contrib.admin import (
    ModelAdmin,
    register
)

from ishelf.books.models import (
    Author,
    Book,
)


@register(Author)
class AuthorAdmin(ModelAdmin):
    list_filter = ["active"]
    list_display = ["__str__", "active"]
    list_editable = ["active"]


@register(Book)
class BookAdmin(ModelAdmin):
    list_filter = ["author", "active"]
    list_display = ["__str__", "active"]
    list_editable = ["active"]
