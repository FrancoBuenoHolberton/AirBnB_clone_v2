#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    #cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """initializesate"""
        super().__init__(*args, **kwargs)

    if models.Typestorage != "db":
        @property
        def cities(self):
            """getter for list of city instances related to theate"""
            lista = []
            allc = models.storage.all(City)
            for city in allc.values():
                if city.state_id == self.id:
                    lista.append(city)
            return lista
