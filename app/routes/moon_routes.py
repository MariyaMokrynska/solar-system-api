from flask import Blueprint, request, make_response, abort
from app.models.moon import Moon
from ..db import db

bp = Blueprint("moons_bp", __name__, url_prefix="/moons")


@bp.post("")
def create_moon():
    request_body = request.get_json()

    try:
        new_moon = Moon.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_moon)
    db.session.commit()

    return make_response(new_moon.to_dict(), 201)


@bp.get("")
def get_all_moons():
    query = db.select(Moon)

    size_param = request.args.get("size")
    if size_param:
        query = query.where(Moon.name.ilike(f"%{size_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Moon.description.ilike(f"%{description_param}%"))

    orbital_period_param = request.args.get("orbital_period")
    if orbital_period_param:
        query = query.where(Moon.orbital_period > 5)

    query = query.order_by(Moon.id)

    moons = db.session.scalars(query)

    moons_response = [moon.to_dict() for moon in moons]

    return moons_response
