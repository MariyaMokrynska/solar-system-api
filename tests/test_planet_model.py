from app.models.planet import Planet
import pytest


def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id=1,
                       name="Mars",
                       description="red planet",
                       moon_count=2)
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "red planet"
    assert result["moon_count"] == 2


def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Mars",
                       description="red planet",
                       moon_count=2)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mars"
    assert result["description"] == "red planet"
    assert result["moon_count"] == 2


def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                       description="red planet",
                       moon_count=2)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "red planet"
    assert result["moon_count"] == 2


def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id=1,
                       name="Mars",
                       moon_count=2)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] is None
    assert result["moon_count"] == 2

##########


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
