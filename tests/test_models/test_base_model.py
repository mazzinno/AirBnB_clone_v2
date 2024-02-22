#!/usr/bin/python3
"""
Test module for BaseModel class.
Tests functionality of BaseModel methods and attributes.
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
import json
import os

class TestBaseModel(unittest.TestCase):
    """Tests the functionality of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Prepares environment for BaseModel tests."""
        try:
            os.rename("file.json", "tmp_file")
        except OSError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Cleans up resources and restores environment after BaseModel tests."""
        try:
            os.remove("file.json")
        except OSError:
            pass
        try:
            os.rename("tmp_file", "file.json")
        except OSError:
            pass
        del cls.storage
        del cls.base

    def test_method_existence(self):
        """Tests if BaseModel has the expected methods."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "delete"))

    def test_attributes_types(self):
        """Tests the types of BaseModel attributes."""
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertIsInstance(self.base.id, str)

    def test_unique_ids_for_different_instances(self):
        """Tests that different instances of BaseModel have unique ids."""
        new_base = BaseModel()
        self.assertNotEqual(self.base.id, new_base.id)
        self.assertLess(self.base.created_at, new_base.created_at)
        self.assertLess(self.base.updated_at, new_base.updated_at)

    def test_to_dict_output(self):
        """Tests the dictionary representation of a BaseModel instance."""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(self.base.id, base_dict["id"])
        self.assertEqual("BaseModel", base_dict["__class__"])
        self.assertEqual(self.base.created_at.isoformat(), base_dict["created_at"])
        self.assertEqual(self.base.updated_at.isoformat(), base_dict["updated_at"])
        self.assertIsNone(base_dict.get("_sa_instance_state"))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Skipping file storage tests when using DBStorage")
    def test_save_method(self):
        """Tests the save method of BaseModel."""
        pre_save_updated_at = self.base.updated_at
        self.base.save()
        self.assertLess(pre_save_updated_at, self.base.updated_at)
        with open("file.json", "r") as file:
            self.assertIn(f"BaseModel.{self.base.id}", file.read())

if __name__ == "__main__":
    unittest.main()
