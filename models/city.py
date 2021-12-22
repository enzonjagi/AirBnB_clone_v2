#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from models.state import State


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    places = relationship('Place')
    state = relationship('State')
