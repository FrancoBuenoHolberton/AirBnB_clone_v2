#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import models
Base = declarative_base()


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.Typestorage == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
