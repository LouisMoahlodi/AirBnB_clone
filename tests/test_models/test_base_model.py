#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        # Test if the id attribute is generated as a string
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        # Test if the created_at attribute is of type datetime
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        # Test if the updated_at attribute is of type datetime
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        # Call the save method
        self.base_model.save()

        # Check if the updated_at attribute is updated correctly
        self.assertEqual(self.base_model.updated_at, self.base_model.created_at)

    def test_to_dict_method(self):
        # Test if the to_dict method returns the expected dictionary
        expected_dict = {
            '__class__': 'BaseModel',
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    def test_to_dict_no_args(self):
        # Tests to_dict() with no arguments.
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_to_dict_excess_args(self):
        # Tests to_dict() with too many arguments.
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_instantiation(self):
        # Tests instantiation with **kwargs.

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_instantiation_dict(self):
        # Tests instantiation with **kwargs from custom dict.
        d = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": str(uuid.uuid4()),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        o = BaseModel(**d)
        self.assertEqual(o.to_dict(), d)

    def test_create_base_model_with_to_dict(self):
        # Create the first BaseModel instance without arguments
        bm1 = BaseModel()
        # Call the .to_dict() method on the first instance to get a dictionary representation
        bm1_dict = bm1.to_dict()
        # Use the dictionary obtained from .to_dict() to create the second BaseModel instance
        bm2 = BaseModel(**bm1_dict)
        # Check if the IDs of bm1 and bm2 are the same
        self.assertEqual(bm1.id, bm2.id)

if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()
