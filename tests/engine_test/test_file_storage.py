import unittest
import os
from unittest.mock import patch
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")  # Clean up after each test

    def test_all_empty_initially(self):
        self.assertEqual(self.file_storage.all(), {})

    def test_new_adds_object(self):
        test_bm = BaseModel()
        self.file_storage.new(test_bm)
        self.assertEqual(self.file_storage.all(), {"BaseModel.{}".format(test_bm.id): test_bm})

    def test_save_stores_objects_to_file(self):
        test_bm1 = BaseModel()
        test_bm2 = BaseModel()
        self.file_storage.new(test_bm1)
        self.file_storage.new(test_bm2)
        self.file_storage.save()

        with open("file.json", "r") as file:
            stored_data = json.load(file)
        self.assertEqual(stored_data, {
            "BaseModel.{}".format(test_bm1.id): test_bm1.to_dict(),
            "BaseModel.{}".format(test_bm2.id): test_bm2.to_dict(),
        })

    @patch("models.engine.os.path.isfile")
    def test_reload_loads_objects_from_file(self, mock_isfile):
        mock_isfile.return_value = True  # Simulate file existence

        test_bm1 = BaseModel(name="Alice")
        test_bm2 = BaseModel(name="Bob")
        with open("file.json", "w") as file:
            json.dump({
                "BaseModel.{}".format(test_bm1.id): test_bm1.to_dict(),
                "BaseModel.{}".format(test_bm2.id): test_bm2.to_dict(),
            }, file)

        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {
            "BaseModel.{}".format(test_bm1.id): test_bm1,
            "BaseModel.{}".format(test_bm2.id): test_bm2,
        })

    def test_reload_handles_missing_file(self):
        self.file_storage.reload()  # No file exists
        self.assertEqual(self.file_storage.all(), {})

if __name__ == '__main__':
    unittest.main()
