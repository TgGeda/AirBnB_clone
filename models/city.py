#!/usr/bin/python3
"""Defines the City class.A class representing a city that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string: name of the city
    """

    state_id = ""
    name = ""
