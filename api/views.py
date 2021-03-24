from ariadne import load_schema_from_path, make_executable_schema
from ariadne.contrib.django.views import GraphQLView
from ariadne.asgi import GraphQL

from .types import TYPES
from .constants import SCHEMAS_DIRECTORY


class GraphQLPlayground(GraphQLView):
    playground_options = {
        "request.credentials": "same-origin",
        "schema.polling.interval": 30000,
        "schema.polling.enable": False,
    }


class DjangoChannelsGraphQL(GraphQL):
    # Workaround from https://github.com/mirumee/ariadne/issues/210
    def __call__(self, scope) -> None:
        async def handle(receive, send):
            await super(DjangoChannelsGraphQL, self).__call__(scope, receive, send)

        return handle


type_defs = load_schema_from_path(SCHEMAS_DIRECTORY)
schema = make_executable_schema(type_defs, TYPES)
graphql_view = GraphQLPlayground.as_view(schema=schema)
channels_view = DjangoChannelsGraphQL(schema=schema, debug=True)
