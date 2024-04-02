
"""Module for FileStorage class."""

import json
import datetime

from models.base_model import BaseModel

class FileStorage:
    """Class for serializing instances to a JSON file and
    deserializing JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return a dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, 'w') as f:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)  

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                file_contents = f.read()
                # Check if the file is empty
                if not file_contents:
                    print("JSON file is empty.")
                    return

                try:
                    data = json.loads(file_contents)
                except json.decoder.JSONDecodeError:
                    # Handle the case of invalid JSON syntax
                    print("JSON file contains invalid syntax.")
                    return

                # Process the loaded data
                for obj in data.values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

