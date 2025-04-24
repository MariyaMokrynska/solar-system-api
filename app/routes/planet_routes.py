from flask import Blueprint, abort, make_response, request
from app.models.planet import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("", strict_slashes=False)
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    # We could also write the line above as:
    # planets = db.session.execute(query).scalars()

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moon_count": planet.moon_count
            }
        )
    return planets_response


@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    moon_count = request_body["moon_count"]

    new_planet = Planet(name=name, description=description,
                        moon_count=moon_count)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "moon_count": new_planet.moon_count
    }
    return response, 201
