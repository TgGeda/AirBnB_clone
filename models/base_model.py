!#/usr/bin/python3
import models
class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args , *kwargs):
        """Initialize public instance attributes"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        """ This code is a part of a method that is used to update the attributes of an object in a database. 

The code checks if there are any keyword arguments (kwargs) passed to the method. 
If there are, it loops through each key-value pair in the kwargs using the items() method. 

For each key-value pair, it checks if the key is either "created_at" or "updated_at".
If it is, it converts the corresponding value to a datetime object using the strptime() method and sets 
the attribute in the object's dictionary (__dict__) to this new datetime object. 

If the key is not "created_at" or "updated_at", 
it simply sets the attribute in the object's dictionary to the corresponding value in the kwargs. 

If there are no keyword arguments passed to the method, 
it adds the object to the database using the new() method from the storage module. """
        
        if len(kwargs) != 0: # checks if there are any keyword arguments (kwargs) passed to the method. 
            for k, v in kwargs.items(): # If there are, it loops through each key-value pair in the kwargs using the items() method. 

                if k == "created_at" or k == "updated_at": # For each key-value pair, it checks if the key is either "created_at" or "updated_at".
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Return string representation of object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """Return dictionary representation of object"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
