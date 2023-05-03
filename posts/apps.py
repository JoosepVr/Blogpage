from django.apps import AppConfig

class PostsConfig(AppConfig):
    name = 'posts'
class MyblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myblog'
