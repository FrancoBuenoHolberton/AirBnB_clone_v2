#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    #places = relationship('Place', cascade="delete, all", backref='cities')
