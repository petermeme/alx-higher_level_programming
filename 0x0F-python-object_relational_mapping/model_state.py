#!/usr/bin/python3
#Defines states using base class(SQLAlchemy)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#declarative_base() callable returns a new base class from which all mapped classes should inherit.
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(50))
