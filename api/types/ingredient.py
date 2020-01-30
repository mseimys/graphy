from ariadne import ObjectType, convert_kwargs_to_snake_case
from django.forms.models import model_to_dict

from products.models import Category, Ingredient
from .query import query
from .mutation import mutation

ingredient = ObjectType("Ingredient")


@query.field("ingredients")
def resolve_ingredients(_, __, offset, limit):
    objects = Ingredient.objects.all()[offset : offset + limit]
    return [model_to_dict(obj) for obj in objects]


@mutation.field("createIngredient")
@convert_kwargs_to_snake_case
def resolve_createIngredient(_, info, input):
    obj, _ = Ingredient.objects.get_or_create(**input)
    return model_to_dict(obj)


@ingredient.field("category")
def resolve_category(obj, *_):
    category = Category.objects.get(id=obj["category"])
    return model_to_dict(category)
