from django.apps import AppConfig


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
