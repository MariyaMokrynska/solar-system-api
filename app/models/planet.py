from sqlalchemy.orm import Mapped, mapped_column
from ..db import db


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    moon_count: Mapped[int]

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                            description=planet_data["description"],
                            moon_count=planet_data["moon_count"])
        return new_planet
