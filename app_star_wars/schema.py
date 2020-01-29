import graphene
from graphene import relay, ObjectType
from graphene.relay import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from app_star_wars.models import Planet, People, Film
from app_star_wars.objects import PlanetNode, PeopleNode,FilmNode
from .mutations.create import CreatePlanet, CreatePeople, CreateFilm


# Define query's and mutation's

class Query(graphene.ObjectType):
    planet = relay.Node.Field(PlanetNode)
    all_planets = DjangoFilterConnectionField(PlanetNode)

    people = relay.Node.Field(PeopleNode)
    all_peoples = DjangoFilterConnectionField(PeopleNode)

    film = relay.Node.Field(FilmNode)
    all_films = DjangoFilterConnectionField(FilmNode)


class Mutation(ObjectType):
    create_planet = CreatePlanet.Field()
    create_people = CreatePeople.Field()
    create_film = CreateFilm.Field()
