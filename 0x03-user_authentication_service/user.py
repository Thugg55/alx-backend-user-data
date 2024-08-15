#!/usr/bin/env python3
""" Create an SQLAlchemy model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base as Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
