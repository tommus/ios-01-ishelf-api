import os

# region Paths

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP_DIR = os.path.join(BASE_DIR, "..", "tmp")

if not os.path.exists(TMP_DIR):
    os.makedirs(TMP_DIR)

# endregion

# region Urls

ROOT_URLCONF = "ishelf.urls"
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# endregion

# region Application definition

INSTALLED_APPS = [

    # region Django

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # endregion

    # region REST

    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_swagger",
    "django_filters",

    # endregion
]

INSTALLED_APPS += [
    "ishelf.authentication.apps.AuthenticationConfig",
    "ishelf.books.apps.BooksConfig",
]

# endregion

# region Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# endregion

# region Templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# endregion

# region Password validation.

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# endregion

# region REST

REST_FRAMEWORK = {

    # Defines what response formats are available from this API.
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),

    # Configures this API is closed and required authentication.
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),

    # Defines default authentication method.
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "ishelf.authentication.BearerAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),

    # Enables path filters.
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
}

# endregion

# region Documentation (Swagger)

LOGIN_URL = "auth:login"
LOGOUT_URL = "auth:logout"

# endregion

# region Miscellaneous

WSGI_APPLICATION = "ishelf.wsgi.application"

# endregion

# region Internationalization

LANGUAGE_CODE = "pl-PL"
TIME_ZONE = "Europe/Warsaw"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "..", "locale"),
)

# endregion
