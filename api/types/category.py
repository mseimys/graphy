from products.models import Category
from .query import query
from .mutation import mutation


@query.field("category")
def resolve_category(_, info, id):
    return Category.objects.get(id=id)


@query.field("categories")
def resolve_categories(_, info, offset, limit):
    return Category.objects.all()[offset : offset + limit]


@mutation.field("createCategory")
def resolve_createCategory(_, info, name):
    obj, _ = Category.objects.get_or_create(name=name)
    return obj
