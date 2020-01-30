from django.forms.models import model_to_dict

from products.models import Category
from .query import query
from .mutation import mutation


@query.field("category")
def resolve_category(_, info, id):
    obj = Category.objects.get(id=id)
    return model_to_dict(obj)


@query.field("categories")
def resolve_categories(_, info, offset, limit):
    objects = Category.objects.all()[offset : offset + limit]
    return [model_to_dict(obj) for obj in objects]


@mutation.field("createCategory")
def resolve_createCategory(_, info, name):
    obj, _ = Category.objects.get_or_create(name=name)
    return model_to_dict(obj)
