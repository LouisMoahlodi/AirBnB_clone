#!/usr/bin/python3
import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({key: value for key, value in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        
        except FileNotFoundError:
            pass
    