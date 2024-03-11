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

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            # If kwargs is empty, create id and created_at attributes
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
        # Include class name in the dictionary
        obj_dict = {'__class__': self.__class__.__name__}
        # Add instance attributes to the dictionary
        obj_dict.update(self.__dict__)
        # Convert creation time to ISO format string
        obj_dict['created_at'] = self.created_at.isoformat()
        # Convert update time to ISO format string
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
if __name__ == "__main__":
    # Create the first BaseModel instance without arguments
    first_base_model = BaseModel()
    # Call the .to_dict() method on the first instance to get a dictionary representation
    first_base_model_dict = first_base_model.to_dict()
    # Use the dictionary obtained from .to_dict() to create the second BaseModel instance
    second_base_model = BaseModel(**{key: value for key, value in first_base_model_dict.items() if key != '__class__'})
