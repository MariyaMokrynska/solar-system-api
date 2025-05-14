from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.models.moon import Moon
from ..db import db
from .route_utilities import validate_model, create_model, get_models_with_filters


bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@bp.delete("/<id>")
def delete_planet(id):
    planet = validate_model(Planet, id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.put("/<id>")
def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon_count = request_body["moon_count"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.get("/<id>")
def get_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()
    # return {
    #     "id": planet.id,
    #     "name": planet.name,
    #     "description": planet.description,
    #     "moon_count": planet.moon_count
    # }


@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)
# @bp.get("", strict_slashes=False)
# def get_all_planets():
#     query = db.select(Planet)

#     name_param = request.args.get("name")
#     if name_param:
#         query = query.where(Planet.name.ilike(f"%{name_param}%"))

#     description_param = request.args.get("description")
#     if description_param:
#         query = query.where(Planet.description.ilike(f"%{description_param}%"))

#     moon_count_param = request.args.get("moon_count")
#     if moon_count_param:
#         query = query.where(Planet.moon_count > 1)

#     query = query.order_by(Planet.id)

#     planets = db.session.scalars(query)

#     planets_response = []
#     for planet in planets:
#         planets_response.append(planet.to_dict())
#         # planets_response.append(
#         #     {
#         #         "id": planet.id,
#         #         "name": planet.name,
#         #         "description": planet.description,
#         #         "moon_count": planet.moon_count
#         #     }
#         # )
#     return planets_response


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

@bp.post("")
def create_planet():
    request_body = request.get_json()
    return create_model(Planet, request_body)

#######


@bp.post("/<planet_id>/moons")
def create_moon_with_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    request_body["planet_id"] = planet.id
    return create_model(Moon, request_body)

# @bp.post("")
# def create_planet():
#     request_body = request.get_json()

#     try:
#         new_planet = Planet.from_dict(request_body)
#         # name = request_body["name"]
#         # description = request_body["description"]
#         # moon_count = request_body["moon_count"]

#         # new_planet = Planet(name=name, description=description,
#         #                     moon_count=moon_count)
#     except KeyError as error:
#         response = {"message": f"Invalid request: missing {error.args[0]}"}
#         abort(make_response(response, 400))

#     db.session.add(new_planet)
#     db.session.commit()

#     # response = {
#     #     "id": new_planet.id,
#     #     "name": new_planet.name,
#     #     "description": new_planet.description,
#     #     "moon_count": new_planet.moon_count
#     # }
#     # return response, 201
#     return new_planet.to_dict(), 201

# # 1 to many


# @bp.post("/<planet_id>/moons")
# def create_moon_with_planet(planet_id):

#     planet = validate_model(Planet, planet_id)

#     request_body = request.get_json()
#     request_body["planet_id"] = planet.id

#     try:
#         new_moon = Moon.from_dict(request_body)

#     except KeyError as error:
#         response = {"message": f"Invalid request: missing {error.args[0]}"}
#         abort(make_response(response, 400))

#     db.session.add(new_moon)
#     db.session.commit()

#     return make_response(new_moon.to_dict(), 201)


@bp.get("/<planet_id>/moons")
def get_moons_by_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    response = [moon.to_dict() for moon in planet.moons]
    return response
