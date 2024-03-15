
"""Module for FileStorage class."""

import json
import os
import datetime
from models.base_model import BaseModel


class FileStorage:
    """Class for serializing instances to a JSON file and
    deserializing JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return a dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(FileStorage.__file_path, 'w') as f:
            obj_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            if not os.path.isfile(FileStorage.__file_path):
                return
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            FileStorage.__objects = {}
# import json
# import os
# import datetime


# class FileStorage:
#     """Class for serializing instances to a JSON file and
#     deserializing JSON file to instances."""

#     __file_path = "file.json"
#     __objects = {}

#     def all(self):
#         """Return a dictionary of all objects."""
#         return FileStorage.__objects

#     def new(self, obj):
#         """Add a new object to the storage."""
#         key = "{}.{}".format(obj.__class__.__name__, obj.id)
#         FileStorage.__objects[key] = obj

#     def save(self):
#         """Serialize __objects to the JSON file __file_path."""
#         with open(FileStorage.__file_path, 'w') as f:
#             json.dump(
#                 {key: value.to_dict() for key, value in
#                  FileStorage.__objects.items()}, f)

#     def reload(self):
#         """Deserialize the JSON file __file_path to __objects, if it exists."""
#         try:
#             with open(FileStorage.__file_path, 'r') as f:
#                 FileStorage.__objects = json.load(f)
#         except FileNotFoundError:
#             FileStorage.__objects = {}
            
    # def reload(self):
    #     """Deserialize the JSON file __file_path to __objects, if it exists."""
    #     try:
    #         with open(FileStorage.__file_path, 'r') as f:
    #             loaded_objects = json.load(f)
    #             for key, value in loaded_objects.items():
    #                 class_name, obj_id = key.split('.')
    #                 # Dynamically get the class using globals()
    #                 cls = globals()[class_name]
    #                 # Instantiate the class using the loaded dictionary
    #                 obj = cls(**value)
    #                 # Add the object to the __objects dictionary
    #                 FileStorage.__objects[key] = obj
    #     except FileNotFoundError:
    #         pass

    
