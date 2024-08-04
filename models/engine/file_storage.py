#!/usr/bin/python3
"""Module for FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Class for serializing instances to a JSON file and deserializing JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return a dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] =obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        dict_storage = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dict_storage, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                dict_storage = json.load(f)
                for obj in dict_storage.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
