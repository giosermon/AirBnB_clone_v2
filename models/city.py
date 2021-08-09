#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    # state_id = Column(String, ForeignKey("States.id"), nullable=False)
