def test_create_one_moon(client):
    # Act
    response = client.post("/moons", json={
        "size": 12334.0,
        "description": "Rocky",
        "orbital_period": 23

    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "size": 12334.0,
        "description": "Rocky",
        "orbital_period": 23
    }


def test_create_one_moon_no_size(client):
    # Arrange
    test_data = {}

    # Act
    response = client.post("/moons", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing size'}


def test_create_one_moon_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "size": 12334.0,
        "description": "Rocky",
        "orbital_period": 23,
        "another": "last value"
    }

    # Act
    response = client.post("/moons", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "size": 12334.0,
        "description": "Rocky",
        "orbital_period": 23
    }


def test_get_all_moons_one_saved_moon(client, one_saved_moon):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "size": 55.6,
        "description": "Rocky",
        "orbital_period": 5
    }


def test_get_all_moons_no_saved_moon(client):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
