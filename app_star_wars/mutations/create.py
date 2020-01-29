from graphene import Field
from graphene import String
from graphene import Mutation

from app_star_wars.models import Planet, People, Film
from app_star_wars.inputs import CreatePlanetInput, CreatePeopleInput, CreateFilmInput
from app_star_wars.utils import transform_global_ids
from app_star_wars.utils import delete_attributes_none
from app_star_wars.objects import PlanetNode, PeopleNode, FilmNode


class CreatePlanet(Mutation):
    planet = Field(PlanetNode)

    class Arguments:
        input = CreatePlanetInput(required=True)

    def mutate(self, info, input):
        planet = Planet.objects.create(**vars(input))

        return CreatePlanet(planet=planet)


class CreatePeople(Mutation):
    people = Field(PeopleNode)

    class Arguments:
        input = CreatePeopleInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        people = People.objects.create(**input)

        return CreatePeople(people=people)


class CreateFilm(Mutation):
    film = Field(FilmNode)

    class Arguments:
        input = CreateFilmInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        film = Film.objects.create(**input)

        return CreateFilm(film=film)
