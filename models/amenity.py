#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import *

class Amenity(BaseModel):
    name = Column(String(128), nullable=False)
    #place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
