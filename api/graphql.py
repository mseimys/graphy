from ariadne import make_executable_schema
from ariadne.asgi import GraphQL

from .resolvers import query
from .schema import type_defs

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)
