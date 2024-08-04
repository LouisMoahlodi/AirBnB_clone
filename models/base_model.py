
"""Defines the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Represents the BaseModel of the Holberton AirBnB project."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Unused
            **kwargs (dict): Key/Values pairs of attributes
        """
        tform = "%Y-%m-%dT%H:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        # Check if kwargs is not empty
        if len(kwargs) != 0:
            # Iterate through the key-value pairs in kwargs
            for attr, value in kwargs.items():
                # Convert created_at and updated_at strings to datetime objects
                if attr == "created_at" or attr == 'updated_at':
                    self.__dict__[attr] = datetime.strptime(value, tform)
                else: 
                    # Set attribute dynamically
                    self.__dict__[attr] = value

        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict
    
    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.dict)
