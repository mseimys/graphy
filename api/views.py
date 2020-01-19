from ariadne import make_executable_schema
from ariadne.contrib.django.views import GraphQLView

from .resolvers import query
from .schema import type_defs

schema = make_executable_schema(type_defs, query)
graphql_view = GraphQLView.as_view(schema=schema)