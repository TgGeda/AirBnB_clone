#!/usr/bin/python3
"""__init__ magic method for models directory. 
The code above is a Python script that initializes the "__init__" magic method for the models directory. 
It imports the "FileStorage" class from the "models.engine.file_storage" module. 

Then, it creates an instance of the "FileStorage" class and assigns it to the variable "storage".
Finally, it calls the "reload" method of the "storage" object to reload any previously saved data."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

