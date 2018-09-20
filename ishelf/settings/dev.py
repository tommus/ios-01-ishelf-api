from ishelf.settings.base import *

# region Secret

SECRET_KEY = "l*rn5-=1zftl3r9#ly4yfd7(je@so3i+eoj@5(6-gwahq@8s)j"

# endregion

# region Debug

DEBUG = True
ALLOWED_HOSTS = ["*"]
APPEND_SLASH = True

# endregion

# region Application definition

INSTALLED_APPS += [
    "django_extensions",
]

# endregion

# region Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(TMP_DIR, "db.sqlite3"),
    }
}

# endregion
