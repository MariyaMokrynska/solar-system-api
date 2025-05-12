from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .moon import Moon


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    moon_count: Mapped[int]
    moon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moon.id"))
    moon: Mapped[Optional["Moon"]] = relationship(back_populates="planets")

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["moon_count"] = self.moon_count

        return planet_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                            description=planet_data["description"],
                            moon_count=planet_data["moon_count"])
        return new_planet
