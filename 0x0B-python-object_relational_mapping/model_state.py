#!/usr/bin/python3
"""sqlalchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class State(Base):
    """this the the model foir state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
            nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
