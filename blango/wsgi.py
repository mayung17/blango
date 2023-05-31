"""
WSGI config for blango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blango.settings')
#DEFINING DJANGO_CONFIGURATION
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

#importing should be after we define DJANGO_CONFIGURATION
from configurations.wsgi import get_wsgi_application


application = get_wsgi_application()
