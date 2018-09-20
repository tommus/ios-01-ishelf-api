from django.urls import path

from ishelf.books import views

# region Application Name

app_name = "books"

# endregion


# region Author

author_list = views.AuthorViewSet.as_view({
    "get": "list",
    "post": "create",
})

author_details = views.AuthorViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

# endregion

# region Book

book_list = views.BookViewSet.as_view({
    "get": "list",
    "post": "create",
})

book_details = views.BookViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

# endregion

# region Patterns

urlpatterns = [
    path("books/", book_list, name="book_list"),
    path("books/<int:pk>/", book_details, name="book_details"),
    path("authors/", author_list, name="author_list"),
    path("authors/<int:pk>/", author_details, name="author_details"),
]

# endregion
