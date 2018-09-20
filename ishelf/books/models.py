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


class Author(Model):
    first_name = CharField(max_length=127, verbose_name=_("First name"))
    last_name = CharField(max_length=127, verbose_name=_("Last name"))
    active = BooleanField(default=True, verbose_name=_("Active"))
    created_at = DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    def __str__(self):
        return str("{} {}".format(self.first_name, self.last_name))


class Book(Model):
    title = CharField(max_length=255, verbose_name=_("Title"))
    subtitle = CharField(max_length=255, verbose_name=_("Subtitle"))
    published = DateTimeField(verbose_name=_("Published"))
    regular_price = DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Regular price"))
    discount_price = DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Discount price"))
    description = TextField(max_length=1023, verbose_name=_("Description"))
    isbn = CharField(max_length=127, verbose_name=_("ISBN"))
    pages = IntegerField(default=1, verbose_name=_("Pages"))
    active = BooleanField(default=True, verbose_name=_("Active"))
    created_at = DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    author = ForeignKey(Author, verbose_name=_("Author"), on_delete=CASCADE)
    cover = ImageField(upload_to="covers", blank=True)

    def __str__(self):
        return str("{} - {}".format(self.title, self.author.__str__()))
