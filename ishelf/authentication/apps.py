from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'ishelf.authentication'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from ishelf.authentication import signals
