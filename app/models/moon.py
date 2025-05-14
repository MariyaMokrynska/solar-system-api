from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .planet import Planet


class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[float] = mapped_column()
    description: Mapped[str] = mapped_column()
    orbital_period: Mapped[float] = mapped_column()  # in days
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")
    # planets: Mapped[list["Planet"]] = relationship(back_populates="moon")

    def to_dict(self):
        # moon_as_dict = {
        #     "id": self.id,
        #     "size": self.size,
        #     "description": self.description,
        #     "orbital_period": self.orbital_period
        # }
        moon_as_dict = {}
        moon_as_dict["id"] = self.id
        moon_as_dict["size"] = self.size
        moon_as_dict["description"] = self.description
        moon_as_dict["orbital_period"] = self.orbital_period

        if self.planet:
            moon_as_dict["planet"] = self.planet.name

        return moon_as_dict

    @classmethod
    def from_dict(cls, moon_data):
        # new_moon = cls(size=moon_data["size"], description=moon_data["description"],
        #                orbital_period=moon_data["orbital_period"])
        planet_id = moon_data.get("planet_id")

        new_moon = cls(
            size=moon_data["size"],
            description=moon_data["description"],
            orbital_period=moon_data["orbital_period"],
            planet_id=planet_id
        )
        return new_moon
