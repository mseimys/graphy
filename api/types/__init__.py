from . import category

from .query import query
from .mutation import mutation
from .ingredient import ingredient
from .subscriptions import subscription

TYPES = [query, mutation, ingredient, subscription]
