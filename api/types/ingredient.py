from ariadne import ObjectType, convert_kwargs_to_snake_case
from graphql import GraphQLResolveInfo

from products.models import Category, Ingredient
from .query import query
from .mutation import mutation

ingredient = ObjectType("Ingredient")


def query_includes(attribute, info):
    try:
        return attribute in [
            selection.name.value
            for selection in info.field_nodes[0].selection_set.selections
        ]
    except:
        pass


@query.field("ingredients")
def resolve_ingredients(queryset, info: GraphQLResolveInfo, offset, limit):
    queryset = Ingredient.objects.all()[offset : offset + limit]
    if query_includes("category", info):
        queryset = queryset.select_related("category")

    return queryset


@mutation.field("createIngredient")
@convert_kwargs_to_snake_case
def resolve_createIngredient(_, info, input):
    obj, _ = Ingredient.objects.get_or_create(**input)
    return obj
