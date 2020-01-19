from django.apps import AppConfig
from django.utils.autoreload import autoreload_started

from .constants import SCHEMAS_DIRECTORY


def reload_graphql_shemas(sender, **kwargs):
    sender.watch_dir(SCHEMAS_DIRECTORY, "*.graphql")


class ApiConfig(AppConfig):
    name = "api"

    def ready(self):
        autoreload_started.connect(reload_graphql_shemas)
