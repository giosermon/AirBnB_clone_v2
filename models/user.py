#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from sqlalchemy.orm import relationship

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade='all, delete-orphan', backref='user')
        # reviews = relationship("Review", cascade='all, delete-orphan', backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
