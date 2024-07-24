from django.apps import AppConfig


class ShopsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shops_app'
    
    def ready(self):
        import shops_app.api.signals
        
