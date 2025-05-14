from app.routes.route_utilities import validate_model, create_model, get_models_with_filters
from werkzeug.exceptions import HTTPException
import pytest
from app.models.planet import Planet
from app.models.moon import Moon


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

# create_model
# We use the `client` fixture because we need an
# application context to work with the database session


def test_create_model_moon(client):
    # Arrange
    test_data = {
        "size": 344.78,
        "description": "Rock",
        "orbital_period": 43
    }

    # Act
    result = create_model(Moon, test_data)

    # # Assert
    # assert result.status_code == 201
    # assert result.get_json() == {
    #     "id": 1,
    #     "size": 344.78,
    #     "description": "Rock",
    #     "orbital_period": 43
    # }
    # Assert
    assert isinstance(result, tuple)
    assert result[0]["id"] == 1
    assert result[0]["size"] == 344
    assert result[0]["description"] == "Rock"
    assert result[0]["orbital_period"] == 43
    assert result[1] == 201


def test_create_model_moon_missing_data(client):
    # Arrange
    test_data = {
        "description": "Rock"
    }

    # Act & Assert
    # Calling `create_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached
    with pytest.raises(HTTPException) as error:
        result_moon = create_model(Moon, test_data)

    response = error.value.response
    assert response.status == "400 BAD REQUEST"


def test_create_model_planet(client):
    # Arrange
    test_data = {
        "name": "Venus"
    }

    # Act
    result = create_model(Planet, test_data)

    # # Assert
    # assert result.status_code == 201
    # assert result.get_json() == {
    #     "id": 1,
    #     "name": "Venus"
    # }
    # Assert
    assert isinstance(result, tuple)
    assert result[0]["id"] == 1
    assert result[0]["name"] == "Venus"
    assert result[1] == 201

# get_model


def test_get_models_with_filters_one_matching_planet(two_saved_planets):
    # Act
    result = get_models_with_filters(Planet, {"name": "Mars"})

    # Assert
    assert result == [{
        "id": 1,
        "name": "Mars",
        "description": "red planet",
        "moon_count": 2
    }]
