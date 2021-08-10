#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv

from sqlalchemy.orm import relationship
from models.state import State
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey(State.id), nullable=False)
        # places = relationship(
        #     "Place", cascade="all, delete-orphan", backref='city')
    else:
        place_id = ""
        user_id = ""
        text = ""
