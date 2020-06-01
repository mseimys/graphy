from ariadne import load_schema_from_path, make_executable_schema
from ariadne.contrib.django.views import GraphQLView

from .types import TYPES
from .constants import SCHEMAS_DIRECTORY


class GraphQLPlayground(GraphQLView):
    playground_options = {
        "request.credentials": "same-origin",
        "schema.polling.enable": False,
    }


type_defs = load_schema_from_path(SCHEMAS_DIRECTORY)
schema = make_executable_schema(type_defs, TYPES)
graphql_view = GraphQLPlayground.as_view(schema=schema)
