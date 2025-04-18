from flask import Blueprint, abort, make_response
from app.models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("", strict_slashes=False)
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            moon_count=planet.moon_count
        ))
    return planets_response

# helper f-n


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response(
            {"message": f"Planet id {planet_id} is invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response(
        {"message": f"Planet id {planet_id} was not found"}, 404))


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "moon_count": planet.moon_count
    }


"""     planet_response = dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            moon_count = planet.moon_count
    )

    return planet_response """
