"""
WSGI config for pontobitmap project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pontobitmap.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pontobitmap.settings')
>>>>>>> 473f429 (inicio)

application = get_wsgi_application()
