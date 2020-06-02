from products.models import Category
from .query import query
from .mutation import mutation


@query.field("category")
def resolve_category(_, info, id):
    return Category.objects.get(id=id)


@query.field("categories")
def resolve_categories(_, info, offset, limit):
    return Category.objects.order_by('-created')[offset : offset + limit]


@mutation.field("createCategory")
def resolve_create_category(_, info, name):
    return Category.objects.create(name=name)

@mutation.field("deleteCategory")
def resolve_delete_category(_, info, id):
    Category.objects.filter(id=id).delete()
    return id
