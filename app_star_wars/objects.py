import graphene
from graphene.relay import Node
from graphene_django import DjangoObjectType

from app_star_wars.models import Planet, People, Film
from .connections import TotalCountConnection
# Define all objects


class PlanetNode(DjangoObjectType):
    class Meta:
        model = Planet
        filter_fields = '__all__'
        interfaces = (Node, )


class PeopleNode(DjangoObjectType):
    class Meta:
        model = People
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'height': ['exact', 'icontains'],
            'mass': ['exact', 'icontains'],
            'hair_color': ['exact', 'icontains'],
            'skin_color': ['exact', 'icontains'],
            'eye_color': ['exact', 'icontains'],
            'birth_year': ['exact', 'icontains'],
            'gender': ['exact', 'icontains'],
            'homeworld': ['exact'],
        }
        
        interfaces = (Node, )


class FilmNode(DjangoObjectType):
    class Meta:
        model = Film
        filter_fields = '__all__'
        interfaces = (Node, )
