#!/usr/bin/python3
"""Defines the Amenity class.A class that representing a amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    Public Attributes:
        name (str): The name of the amenity.
    """

    name = ""
