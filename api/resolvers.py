import json

from ariadne import QueryType, MutationType
from django.forms.models import model_to_dict

from products.models import Category

query = QueryType()
mutation = MutationType()


@query.field("hello")
def resolve_hello(_, info):
    request = info.context
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello, %s!" % user_agent


@query.field("getCategory")
def resolve_getCategory(_, info, id):
    obj = Category.objects.get(id=id)
    return model_to_dict(obj)


@query.field("categories")
def resolve_categories(_, info, offset, limit):
    objects = list(Category.objects.all()[offset : offset + limit])
    return [model_to_dict(obj) for obj in objects]


@mutation.field("createCategory")
def resolve_createCategory(_, info, name):
    obj, _ = Category.objects.get_or_create(name=name)
    return model_to_dict(obj)
