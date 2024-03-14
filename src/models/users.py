# pylint: disable=redefined-builtin

""" User model Module
This module is responsible for manager all users data.
"""

from sqlalchemy.orm import declarative_base

from db import db

Base = declarative_base()

class UserModel(db.Model):
    """ User model
    This model contains user mappers informations.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
