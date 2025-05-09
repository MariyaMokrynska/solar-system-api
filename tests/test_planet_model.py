from app.models.planet import Planet
import pytest


def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "Earth",
        "description": "blue planet",
        "moon_count": 1
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Earth"
    assert new_planet.description == "blue planet"


def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "red planet",
        "moon_count": 3
    }

    # Act & Assert
    with pytest.raises(KeyError, match='name'):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Saturn",
        "moon_count": 3
    }

    # Act & Assert
    with pytest.raises(KeyError, match='description'):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "Mercury",
        "description": "1st planet",
        "moon_count": 2
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mercury"
    assert new_planet.description == "1st planet"
