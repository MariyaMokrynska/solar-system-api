from werkzeug.exceptions import HTTPException
from app.routes.route_utilities import validate_model
import pytest
from app.models.planet import Planet


def test_validate_planet(two_saved_planets):
    # Act
    # result_planet = validate_planet(1)

    result_planet = validate_model(Planet, 1)

    # Assert
    assert result_planet.id == 1
    assert result_planet.name == "Mars"
    assert result_planet.description == "red planet"
    assert result_planet.moon_count == 2


def test_validate_planet_missing_record(two_saved_planets):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "3")


def test_validate_planet_invalid_id(two_saved_planets):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "cat")
