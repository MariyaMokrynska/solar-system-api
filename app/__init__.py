from flask import Flask
from .routes.planet_routes import planets_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(planets_bp)
    return app
#http://127.0.0.1:5000/planets
