"""
WSGI config for marmitex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

from __future__ import absolute_import

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marmitex.settings")

application = get_wsgi_application()

if not settings.DEBUG:
    application = WhiteNoise(application, root="/static/")
    application.add_files("/static/")
