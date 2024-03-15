#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model_dict = self.base_model.to_dict()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        # Test if all() returns the dictionary __objects
        objects = self.file_storage.all()
        self.assertEqual(objects, {})

    def test_new(self):
        # Test if new() sets in __objects the obj with key <obj class name>.id
        self.file_storage.new(self.base_model)
        objects = self.file_storage.all()
        self.assertIn("BaseModel." + self.base_model.id, objects)
        self.assertEqual(objects["BaseModel." +
                                 self.base_model.id], self.base_model_dict)

    def test_save(self):
        # Test if save() serializes __objects to the JSON file (path:
        # __file_path)
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        # Test if reload() deserializes the JSON file to __objects
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertIn("BaseModel." + self.base_model.id, objects)
        self.assertEqual(objects["BaseModel." +
                                 self.base_model.id], self.base_model_dict)


if __name__ == '__main__':
    unittest.main()
