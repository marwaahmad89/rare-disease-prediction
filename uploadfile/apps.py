from distutils.command import config
from django.apps import AppConfig


class UploadfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Table Management'

class Mainconfig(AppConfig):
    name='main'
    Verbose_name='Table Management'

