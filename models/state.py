#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", cascade="all, delete-orphan", backref='state')
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with state_id"""
            from models import storage
            from models.city import City
            items = storage.all(City).items()
            result = []
            for _, value in items:
                if value.state_id == self.id:
                    result.append(value)
            return (result)
