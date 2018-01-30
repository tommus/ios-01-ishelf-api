from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from ishelf.books.views import (
    AuthorViewSet,
    BookViewSet,
    BookBookmarkViewSet,
    BookRateViewSet,
)

router = routers.DefaultRouter()
router.register(r'books/authors', AuthorViewSet)
router.register(r'books/books', BookViewSet)
router.register(r'books/bookmarks', BookBookmarkViewSet)
router.register(r'books/rates', BookRateViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', get_swagger_view(title='iShelf API'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'iShelf API'
admin.site.site_header = 'iShelf API'
