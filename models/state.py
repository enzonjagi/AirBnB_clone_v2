#!/usr/bin/python3
""" State Module for HBNB project """
from os import get_terminal_size
from models.base_model import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City')

    def get_cities(self):
        '''
        a getter attribute to return list if City instances
        with state_id equal to the current State.id
        '''
        return
