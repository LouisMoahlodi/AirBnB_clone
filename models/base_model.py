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
            # Iterate through the key-value pairs in kwargs
            for attr, value in kwargs.items():
                # Convert created_at and updated_at strings to datetime objects
                if attr in ['created_at', 'updated_at']:
                    date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[attr] = value

                else: 
                    # Set attribute dynamically
                    self.__dict__[attr] = value
        else:
            # If kwargs is empty, create id and created_at attributes
            self.__dict__['id'] = str(uuid.uuid4())
            self.__dict__['created_at'] = datetime.now()
            self.__dict__['updated_at'] = datetime.now()

        # Generate a unique UUID for the instance
        self.id = str(uuid.uuid4())
        # Set creation time to current time
        self.created_at = datetime.now()
        # Initially set update time to creation time
        self.updated_at = self.created_at

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
        # Update update time to current time
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
        dict: Dictionary representation of the BaseModel instance.
        """
        # Add instance attributes to the dictionary
        obj_dict = self.__dict__.copy()
        
        # Remove the __class__ attribute if present
        obj_dict.pop('__class__', None)
        
        # Convert creation time to ISO format string
        obj_dict['created_at'] = self.created_at.isoformat()
        
        # Convert update time to ISO format string
        obj_dict['updated_at'] = self.updated_at.isoformat()
    
        return obj_dict

    