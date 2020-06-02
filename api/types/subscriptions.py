import asyncio
from ariadne import SubscriptionType

subscription = SubscriptionType()


@subscription.source("counter")
async def counter_generator(obj, info):
    for i in range(5):
        await asyncio.sleep(1)
        yield i


@subscription.field("counter")
def counter_resolver(count, info):
    return count + 1


# DO NOT WORK
@subscription.source("categoryAdded")
async def category_added_generator(obj, info):
    for i in range(5):
        await asyncio.sleep(1)
        yield i


# DO NOT WORK
@subscription.field("categoryAdded")
def category_added_resolver(count, info):
    return count + 1
