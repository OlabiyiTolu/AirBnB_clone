#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.test_bm = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.test_bm.id)
        self.assertIsNotNone(self.test_bm.created_at)
        self.assertIsNotNone(self.test_bm.updated_at)

    def test_id(self):
        """
        Tests if the id is unique
        """
        another_bm = BaseModel()
        self.assertNotEqual(self.test_bm.id, another_bm.id)

    def test_save(self):
        """
        Tests the save method
        """
        initial_time = self.test_bm.updated_at
        updated_time = self.test_bm.save()

        self.assertNotEqual(initial_time, updated_time)
        
    def test_timestamp(self):
        """
        Test the timestamp are datetime object
        """
        created_at = self.test_bm.created_at
        updated_at = self.test_bm.updated_at
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)


    def test_to_dict(self):
        """
        Test the dictionary function
        """
        dict_test_bm = self.test_bm.to_dict()
        self.assertIsInstance(dict_test_bm, dict)

        self.assertEqual(dict_test_bm["__class__"], "BaseModel")
        self.assertEqual(dict_test_bm["id"], self.test_bm.id)
        self.assertEqual(dict_test_bm["created_at"], self.test_bm.created_at.isoformat())
        self.assertEqual(dict_test_bm["updated_at"], self.test_bm.updated_at.isoformat())

    def test_str(self):
        test_bm = BaseModel()

        self.assertTrue(str(test_bm).startswith("[BaseModel]"))
        self.assertIn(test_bm.id, str(test_bm))
        self.assertIn(str(test_bm.__dict__), str(test_bm))

if __name__ == "__main__":
    unittest.main()
