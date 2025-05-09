# From Set up: Create a test to check GET /planets returns 200 and an empty array.
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# 2. GET /planets/1 with no data in test database (no fixture) returns a 404


def test_no_get_planet_error(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    # assert response_body == {
    #     "id": "",
    #     "name": "",
    #     "description": "",
    #     "moon_count": ""
    # }

# 1. GET /planets/1 returns a response body that matches our fixture


def test_get_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "red planet",
        "moon_count": 2
    }

# 3. GET /planets with valid test data (fixtures) returns a 200 with an array including appropriate test data


def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Mars",
            "description": "red planet",
            "moon_count": 2
        },
        {
            "id": 2,
            "name": "Earth",
            "description": "blue planet",
            "moon_count": 1
        }
    ]

# 4. POST /planets with a JSON request body returns a 201


def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Saturn",
        "description": "rings",
        "moon_count": 7
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "description": "rings",
        "moon_count": 7
    }
########
# test get_planet


def test_get_all_planets_with_two_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Mars",
        "description": "red planet",
        "moon_count": 2
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Earth",
        "description": "blue planet",
        "moon_count": 1
    }


def test_get_all_planets_with_name_query_matching_none(client, two_saved_planets):
    # Act
    data = {"name": "Venus",
            "moon_count": 3}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_all_planets_with_name_query_matching_one(client, two_saved_planets):
    # Act
    data = {"name": "Mars",
            "description": "red planet",
            "moon_count": 2}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "Mars",
        "description": "red planet",
        "moon_count": 2
    }


def test_get_one_planet_succeeds(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "red planet",
        "moon_count": 2
    }


def test_get_one_planet_missing_record(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "planet 3 not found"}


def test_get_one_planet_invalid_id(client, two_saved_planets):
    # Act
    response = client.get("/planets/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "planet cat invalid"}


###########
# test create_planet


def test_create_one_planet_no_name(client):
    # Arrange
    test_data = {"description": "some planet",
                 "moon_count": 3}

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}


def test_create_one_planet_no_description(client):
    # Arrange
    test_data = {"name": "Saturn",
                 "moon_count": 3}

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing description'}


def test_create_one_planet_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "Venus",
        "description": "The Best!",
        "moon_count": 5
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "The Best!",
        "moon_count": 5
    }
