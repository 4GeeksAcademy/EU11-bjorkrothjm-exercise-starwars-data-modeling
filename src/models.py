import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# First model 
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"), unique=True)
    favorite = relationship("Favorite", backref="user")

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = relationship("User", backref="favorite")

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"), unique=False)
    favorite = relationship("Favorite", backref="planet")

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"), unique=False)
    favorite = relationship("Favorite", backref="character")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"), unique=False)
    favorite = relationship("Favorite", backref="vehicle")

# Model 2
class User2(Base):
    __tablename__ = 'user2'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite2.id"), unique=True)
    favorite = relationship("Favorite2", backref="user")

class Favorite2(Base):
    __tablename__ = 'favorite2'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = relationship("User2", backref="favorite2")
    favorite_junction_relation = relationship('favorite_junction', backref="favorite2")


class Favorite_Junction(Base):
    __tablename__ = 'favorite_junction'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite2.id'), unique=True)

"""
favorite_junction = Table('favorite_junction', Base.metadata,
                            Column('planet2', Integer),
                            Column('character2', Integer, ForeignKey('character2.id')),
                            Column('vehicle2', Integer, ForeignKey('vehicle2.id')),
                            Column('favorite2', Integer, ForeignKey('favorite2.id'), unique=True)
                            )
"""

class Planet2(Base):
    __tablename__ = 'planet2'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_junction_id = Column(Integer, ForeignKey('favorite_junction.id'))
    favorite_junction_relation = relationship('favorite_junction', backref="planet2")

class Character2(Base):
    __tablename__ = 'character2'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_junction_id = Column(Integer, ForeignKey('favorite_junction.id'))
    favorite_junction_relation = relationship('favorite_junction', backref="character2")


class Vehicle2(Base):
    __tablename__ = 'vehicle2'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_junction_id = Column(Integer, ForeignKey('favorite_junction.id'))
    favorite_junction_relation = relationship('favorite_junction', backref="vehicle2")





""" 
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    relation = relationship("User_Favorite_Junction")

class User_Favorite_Junction(Base):
    __tablename__ = 'user_favorite_junction'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer,  ForeignKey('user.id'), primary_key=True)
    favorite_id = Column(Integer, ForeignKey('favorite.id'), primary_key=True)
    

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('favorite.id'), primary_key=True)
    name = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('favorite.id'), primary_key=True)
    name = Column(String(250), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('favorite.id'), primary_key=True)
    name = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

"""

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
