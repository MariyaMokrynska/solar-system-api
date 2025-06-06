import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.planet import Planet
from app.models.moon import Moon

load_dotenv()


@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mars_planet = Planet(name="Mars",
                         description="red planet",
                         moon_count=2)
    earth_planet = Planet(name="Earth",
                          description="blue planet",
                          moon_count=1)

    db.session.add_all([mars_planet, earth_planet])
    db.session.commit()


@pytest.fixture
def one_saved_moon(app):
    moon = Moon(size=55.6, description="Rocky",
                orbital_period=5)
    db.session.add(moon)
    db.session.commit()
