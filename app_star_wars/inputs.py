from graphene import ID
from graphene import String
from graphene import InputObjectType


# Create your inputs types here.


class CreatePlanetInput(InputObjectType):
    name = String(required=True)
    rotation_period = String(required=True)
    orbital_period = String(required=True)
    diameter = String(required=True)
    climate = String(required=True)
    gravity = String(required=True)
    terrain = String(required=True)
    surface_water = String(required=True)
    population = String(required=True)


class CreatePeopleInput(InputObjectType):
    name = String(required=True)
    height = String(required=True)
    mass = String(required=True)
    hairColor = String(required=True)
    skinColor = String(required=True)
    eyeColor = String(required=True)
    birthYear = String(required=True)
    gender = String(required=True)
    homeworld = ID(required=True)


class CreateFilmInput(InputObjectType):
    title = String(required=True)
    episodeId = String(required=True)
    openingCrawl = String(required=True)
    director = String(required=True)
    producer = String(required=True)
    releaseDate = String(required=True)
    characters = ID(required=True)
    planets = ID(required=True)


class UpdatePlanetInput(InputObjectType):
    id = ID(required=True)
    name = String()
    rotation_period = String()
    orbital_period = String()
    diameter = String()
    climate = String()
    gravity = String()
    terrain = String()
    surface_water = String()
    population = String()
