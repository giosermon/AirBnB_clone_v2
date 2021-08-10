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
        cities = relationship("City")
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with state_id"""
            from models import storage
            from models.city import City
            items = storage.all(City).items()
            return [obj for _, obj in items if obj.state_id == self.id]

        @property
        def cities(self):
            """return all cities"""
            from models import storage
            result = []
            for city in storage.all(City):
                result.append(city)
