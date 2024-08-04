import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class represents a base model for other classes.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Time when an instance is created.
        updated_at (datetime): Time when an instance is updated.

    Methods:
        __init__: Initializes a new BaseModel instance.
        __str__: Returns a string representation of the BaseModel instance.
        save: Updates the updated_at attribute with the current datetime.
        to_dict: Returns a dictionary representation of the BaseModel instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Sets the id attribute to a unique UUID, created_at and updated_at
        attributes to the current datetime.
        """
        # Check if kwargs is not empty
        if kwargs:
            for attr, value in kwargs.items():
                if attr in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, attr, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
