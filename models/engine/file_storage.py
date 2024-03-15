#!/usr/bin/python3
"""Module for FileStorage class."""

import json
import os
import datetime


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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {key: value for key, value in
                 FileStorage.__objects.items()}, f)

    def reload(self):
        """ Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    # Get the class name and ID from the key
                    class_name, obj_id = key.split('.')
                    # Create an instance of the class using eval
                    obj_cls = eval(class_name)
                    # Create a new instance of the class with the attributes from the loaded data
                    obj = obj_cls(**value)
                    # Add the object to __objects
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
