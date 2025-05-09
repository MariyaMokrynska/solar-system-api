from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@planets_bp.put("/<id>")
def update_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon_count = request_body["moon_count"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


def validate_planet(id):
    try:
        id = int(id)
    except:
        response = {"message": f"planet {id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet {id} not found"}
        abort(make_response(response, 404))

    return planet


@planets_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_planet(id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "moon_count": planet.moon_count
    }


@planets_bp.get("", strict_slashes=False)
def get_all_planets():
    query = db.select(Planet)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    moon_count_param = request.args.get("moon_count")
    if moon_count_param:
        query = query.where(Planet.moon_count > 1)

    query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

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


# @planets_bp.get("", strict_slashes=False)
# def get_all_planets():
#     query = db.select(Planet).order_by(Planet.id)
#     planets = db.session.scalars(query)
#     # We could also write the line above as:
#     # planets = db.session.execute(query).scalars()

#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "moon_count": planet.moon_count
#             }
#         )
#     return planets_response


@planets_bp.post("")
def create_planet():
    request_body = request.get_json()

    try:
        new_planet = Planet.from_dict(request_body)
        # name = request_body["name"]
        # description = request_body["description"]
        # moon_count = request_body["moon_count"]

        # new_planet = Planet(name=name, description=description,
        #                     moon_count=moon_count)
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "moon_count": new_planet.moon_count
    }
    return response, 201
