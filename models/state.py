#!/usr/bin/python3
"""Defines the State class.A class representing a state that inherits from BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Public class attributes:

    name: A string representing the name of the state. 
    Default is an empty string.
    """

    name = ""
