# Represent database models

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    country_id = Column(Integer, ForeignKey("countries.id"))
    supermarket_id = Column(Integer, ForeignKey("supermarkets.id"))

    country = relationship("Country", back_populates="places")
    supermarket = relationship("Supermarket", back_populates="places")

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    places = relationship("Place", back_populates="country")

class Supermarket(Base):
    __tablename__ = "supermarkets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    places = relationship("Place", back_populates="supermarket")