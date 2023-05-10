!#/usr/bin/python3

class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        """Initialize public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of object"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
