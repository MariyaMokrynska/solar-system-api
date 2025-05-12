from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .planet import Planet


class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[float] = mapped_column()
    description: Mapped[str] = mapped_column()
    orbital_period: Mapped[float] = mapped_column()  # in days
    planets: Mapped[list["Planet"]] = relationship(back_populates="moon")

    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "size": self.size,
            "description": self.description,
            "orbital_period": self.orbital_period
        }

        return moon_as_dict

    @classmethod
    def from_dict(cls, moon_data):
        new_moon = cls(size=moon_data["size"], description=moon_data["description"],
                       orbital_period=moon_data["orbital_period"])
        return new_moon
