from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view

# region Patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("rest_framework.urls", namespace="auth")),
    path("api/docs/", get_swagger_view(title="Interview API")),
    path("api/auth/token/", views.obtain_auth_token, name="token"),
    path("api/bookstore/", include("ishelf.books.urls", namespace="bookstore")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# endregion

# region Configuration

admin.site.site_title = "Interview API"
admin.site.site_header = "Interview API"

# endregion
