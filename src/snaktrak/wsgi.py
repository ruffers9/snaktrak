"""
WSGI config for django-react-redux-base project.

"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snaktrak.settings.prod")

application = get_wsgi_application()
