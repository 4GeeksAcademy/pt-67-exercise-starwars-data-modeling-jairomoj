import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(12), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    eye_color = Column(String(40), nullable=False)
    hair_color = Column(String(40), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}
    
class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(40), nullable=False)
    _class = Column(String(40), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}
    
class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(40), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}
    
class Fav_character(Base):
    __tablename__ = 'fav_character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    char_relation = Column(Integer, ForeignKey('character.id'), nullable=False)
    user_relation = Column(Integer, ForeignKey('user.id'), nullable=False)

    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}
    
class Fav_vehicle(Base):
    __tablename__ = 'fav_vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehic_relation = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    user_relation = Column(Integer, ForeignKey('user.id'), nullable=False)

    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}
    
class Fav_planet(Base):
    __tablename__ = 'fav_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_relation = Column(Integer, ForeignKey('planet.id'), nullable=False)
    user_relation = Column(Integer, ForeignKey('user.id'), nullable=False)

    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
