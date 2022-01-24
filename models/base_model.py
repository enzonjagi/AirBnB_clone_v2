#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from ast import Str
from re import S
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import delete, null
from sqlalchemy.sql.sqltypes import DATETIME, DateTime
from models import storage_type


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(
        String(60), unique=True, nullable=False,
        primary_key=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for kwarg in kwargs:
                if kwarg in ['created_at', 'updated_at']:
                    setattr(self, kwarg, datetime.fromisoformat(kwargs[kwarg]))
                elif kwarg != '__class__':
                    setattr(self, kwarg, kwargs[kwarg])

                if storage_type == 'db':
                    if not hasattr(kwargs, 'id'):
                        setattr(self, 'id', str(uuid.uuid4()))
                    if not hasattr(kwargs, 'created_at'):
                        setattr(self, 'created_at', datetime.now())
                    if not hasattr(kwargs, 'updated_at'):
                        setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary['_sa_instance_state'] is not None:
            dictionary['_sa_instance_state'].delete(self.__dict__)
        return dictionary

    def delete(self):
        '''Delete current instance from the storage'''
        from models import storage
        # should call the delete method
        storage.delete(self)
