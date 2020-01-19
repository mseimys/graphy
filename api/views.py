from ariadne import load_schema_from_path, make_executable_schema
from ariadne.contrib.django.views import GraphQLView

from .resolvers import query, mutation
from .constants import SCHEMAS_DIRECTORY

type_defs = load_schema_from_path(SCHEMAS_DIRECTORY)

schema = make_executable_schema(type_defs, [query, mutation])
graphql_view = GraphQLView.as_view(schema=schema)
