#!/usr/bin/python3
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    setattr(self, k,
                            datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif k != '__class__':
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        newDict = self.__dict__.copy()
        if '_sa_instance_state' in newDict:
            del newDict['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, newDict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        from models import storage
        storage.delete(self)
