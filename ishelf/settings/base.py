import os

# Paths.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP_DIR = os.path.join(BASE_DIR, '..', 'tmp')

if not os.path.exists(TMP_DIR):
    os.makedirs(TMP_DIR)

# Urls.
ROOT_URLCONF = 'ishelf.urls'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(TMP_DIR, 'media')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i4ox_3jd^)tgv%yjauy-&6f(mzf$i8&of%)9(cmf8=$djl_h-*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Databases.
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TMP_DIR, 'db.sqlite3'),
    }
}

# Application definition.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'ishelf.authentication.apps.AuthenticationConfig',
    'ishelf.books.apps.BooksConfig',
]

# Middleware (security, session, localization, authentication, etc.).
# # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Template engine configuration.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation.
# https://docs.djangoproject.com/en/2.0/topics/auth/passwords/
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# REST configuration.
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {

    # Defines what response formats are available from this API.
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_jsonp.renderers.JSONPRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework_yaml.renderers.YAMLRenderer',
    ),

    # Defines what request formats are accepted while accessing this API.
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework_xml.parsers.XMLParser',
        'rest_framework_yaml.parsers.YAMLParser',
    ),

    # Configures this API is closed and required authentication.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    # Defines default authentication method.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'ishelf.authentication.authentication.BearerAuthentication',
    ),

    # Enables path filters.
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_filters.backends.DjangoFilterBackend',
    ),

    # Configures pagination.
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Misc.
WSGI_APPLICATION = 'ishelf.wsgi.application'

# Internationalization.
LANGUAGE_CODE = 'pl-PL'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, '..', 'locale'),
)
