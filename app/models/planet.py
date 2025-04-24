from sqlalchemy.orm import Mapped, mapped_column
from ..db import db


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    moon_count: Mapped[int]


# class Planet:
#     def __init__(self, id, name, description, moon_count):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moon_count = moon_count

# planets = [
#     Planet(3, "Earth", "The only planet known to support life.", 1),
#     Planet(4, "Mars", "Known as the Red Planet", 2),
#     Planet(5, "Jupiter", "Gas giant", 95),
#     Planet(6, "Saturn", "Famous for its prominent ring system.", 83)
# ]
