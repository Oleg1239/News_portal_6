from django.apps import AppConfig

class EconomicalNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'economical_news'
    verbose_name = 'Экономические Новости'

    def ready(self):
        import economical_news.signals
