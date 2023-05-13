#!/usr/bin/python3
"""Defines the Place class.A class representing a place that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
  
    """Represent a place.
    Public Attributes:
        Public class attributes:
         city_id: string - empty string: it will be the City.id
         user_id: string -  empty string: it will be the User.id
         name: string - empty string that represent The name of the place
         description: string - empty string that represent The description of the place
         number_rooms: integer - 0 that reprsent The number of rooms of the place
         number_bathrooms: integer - 0 that reprsent The number of bathrooms of the place
         max_guest: integer - 0 that reprsent The maximum number of gusts of the place
         price_by_night: integer - 0 that reprsent The price by night of the place
         latitude: float - 0.0  that reprsent The The latitude of the place.
         longitude: float - 0.0 that reprsent The The The longitude of the place.
         amenity_ids: list of string - empty list: it will be the list of Amenity.id holds A list of Amenity ids. later
    """

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []
     
 
