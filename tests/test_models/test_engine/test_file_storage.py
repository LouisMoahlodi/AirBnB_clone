#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj3 = BaseModel()
        self.obj1.save()
        self.obj2.save()
        self.obj3.save()

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)

    def test__file_path(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test__objects(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(len(FileStorage._FileStorage__objects), 3)

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 3)
        self.assertIn('BaseModel.' + self.obj1.id, all_objs)
        self.assertIn('BaseModel.' + self.obj2.id, all_objs)
        self.assertIn('BaseModel.' + self.obj3.id, all_objs)

    def test_new(self):
        obj4 = BaseModel()
        self.storage.new(obj4)
        self.assertIn('BaseModel.' + obj4.id, self.storage.all())

    def test_save_and_reload(self):
        # Save objects
        self.storage.save()
        # Clear objects
        self.storage._FileStorage__objects = {}
        # Reload objects
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 3)
        self.assertIn('BaseModel.' + self.obj1.id, all_objs)
        self.assertIn('BaseModel.' + self.obj2.id, all_objs)
        self.assertIn('BaseModel.' + self.obj3.id, all_objs)

if __name__ == '__main__':
    unittest.main()
