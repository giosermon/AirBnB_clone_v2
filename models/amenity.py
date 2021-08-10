#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import Base, BaseModel
from models.place import place_amenity


class Amenity(BaseModel, Base):
    '''amenities object representation'''
    __tablename__ = 'amenities'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
