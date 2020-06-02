"""
ASGI config for graphy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from api.views import channels_view

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graphy.settings")


application = ProtocolTypeRouter(
    {"websocket": URLRouter([path("graphql/", channels_view)])}
)
