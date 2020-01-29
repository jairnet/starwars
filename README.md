# Example GraphQL with Django

This application has queries and mutations of Star Wars.

## Steps required to start the application

1.  It is recommended to use **Python 3.4** or higher
2.  Install the packages contained in **requirements.txt** using the command    installation of `pip install -r requirements.txt`
3.  Execute the run.py file with `python manage.py makemigrations`
4.  Execute the run.py file with `python manage.py migrate`
5.  Execute the run.py file with `python manage.py runserver`
6.  For load data fixtures execute:
    python ./manage.py loaddata planets
    python ./manage.py loaddata people
    python ./manage.py loaddata transport
    python ./manage.py loaddata starships
    python ./manage.py loaddata vehicles
    python ./manage.py loaddata species
    python ./manage.py loaddata films
7.  Open the browser and go to the address <http://localhost:8000/> or <http://127.0.0.1:8000/>

---

# Queries

## Query find for name or contain 
```
query {
  allPeoples(name_Icontains: "Luke") {
    edges {
      node {
        name,
        height,
        mass,
        hairColor,
        skinColor,
        eyeColor
        birthYear,
        gender,
      }
    }
  }
}
```

## All peoples whit id, name and birth year
```
query {
  allPeoples {
    edges {
      node {
        id,
        name,
        birthYear
      }
    }
  }
}
```

## All planets whit id and name
```
query {
  allPlanets {
    edges {
      node {
        id,
        name
      }
    }
  }
}
```

## People and origin planet
```
query {
  allPeoples {
    edges {
      node {
        name,
        height,
        mass,
        hairColor,
        skinColor,
        eyeColor
        birthYear,
        gender,
        homeworld {
          name,
          rotationPeriod,
          orbitalPeriod,
          diameter,
          climate,
          gravity,
          terrain,
          surfaceWater,
          population
        }
      }
    }
  }
}
```

## Films and People and origin planet
```
query {
  allFilms {
    edges {
      node {
        title,
        episodeId,
        openingCrawl,
        director,
        producer,
        releaseDate,
        characters {
          edges {
            node {
              name,
              height,
              mass,
              hairColor,
              skinColor,
              eyeColor
              birthYear,
              gender,
            }
          }
        }
      planets {
        edges {
          node {
            name,
          	rotationPeriod,
          	orbitalPeriod,
          	diameter,
          	climate,
          	gravity,
          	terrain,
          	surfaceWater,
          	population
          }
        }
      }
        
      }
    }
  }
}
```

## Mutation: Create planet
```
mutation {
  createPlanet(input: {
    	name: "Tierra",
  		rotationPeriod: "24",
  		orbitalPeriod: "365",
      diameter: "12.742",
      climate: "4",
      gravity: "9.8",
      terrain: "6",
      surfaceWater: "7",
      population: "8"}) {
    planet {
      name
      rotationPeriod
      orbitalPeriod
      diameter
      climate
      gravity
      terrain
      surfaceWater
      population
    }
  }
}
```
