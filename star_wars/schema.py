from graphene import Schema

from app_star_wars.schema import Mutation
from app_star_wars.schema import Query


schema = Schema(query=Query, mutation=Mutation)
