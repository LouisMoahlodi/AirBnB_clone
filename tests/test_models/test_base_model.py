#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
from datetime import datetime
from datetime import timedelta
from unittest.mock import patch
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

    @patch('datetime.datetime')
    def test_save_method(self, mock_datetime):
        # Mock datetime object
        mock_now = datetime(2022, 3, 8, 10, 30)
        mock_datetime.now.return_value = mock_now

        # Call the save method
        self.base_model.save()

        # Check if the updated_at attribute is updated correctly
        self.assertEquals(self.base_model.updated_at, mock_now)

    def test_to_dict_method(self):
        # Test if the to_dict method returns the expected dictionary
        expected_dict = {
            '__class__': 'BaseModel',
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()