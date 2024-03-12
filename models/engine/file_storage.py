
import json
import os
import datetime

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: value for key, value in FileStorage.__objects.items()}, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        
        except FileNotFoundError:
            pass
    