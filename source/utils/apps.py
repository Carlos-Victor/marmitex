from __future__ import absolute_import

from django.apps import AppConfig
from django.db.models.signals import post_migrate


class UtilsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "utils"

    def ready(self):
        from .signals import populate_permissions

        post_migrate.connect(populate_permissions, sender=self)
