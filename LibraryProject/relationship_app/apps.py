from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
    
    # Remove the ready() method or comment it out
    # def ready(self):
    #    import relationship_app.signals
