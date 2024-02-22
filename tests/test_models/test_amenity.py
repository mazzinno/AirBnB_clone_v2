#!/usr/bin/python3
"""
Tests for the Amenity class documentation and functionality.
"""

from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
Amenity = amenity.Amenity

class TestAmenityDocs(unittest.TestCase):
    """Doc and style tests for Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Prepare for doc tests."""
        cls.amenity_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Check PEP8 for amenity.py."""
        result = pep8.StyleGuide(quiet=True).check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 issues in amenity.py.")

    def test_pep8_conformance_test_amenity(self):
        """Check PEP8 for test_amenity.py."""
        result = pep8.StyleGuide(quiet=True).check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 issues in test_amenity.py.")

    def test_module_docstring(self):
        """Ensure amenity.py has a docstring."""
        self.assertTrue(amenity.__doc__, "Missing docstring in amenity.py.")

    def test_class_docstring(self):
        """Check for Amenity class docstring."""
        self.assertTrue(Amenity.__doc__, "Missing Amenity class docstring.")

    def test_func_docstrings(self):
        """Verify docstrings in Amenity methods."""
        for func in self.amenity_funcs:
            self.assertTrue(func[1].__doc__, f"{func[0]} missing docstring.")

class TestAmenity(unittest.TestCase):
    """Functionality tests for Amenity."""

    def test_is_subclass(self):
        """Verify Amenity is subclass of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_name_attr(self):
        """Test Amenity has attr name, checks if empty or None based on storage."""
        amenity = Amenity()
        expected = None if models.storage_t == 'db' else ""
        self.assertEqual(amenity.name, expected)

    def test_to_dict_creates_dict(self):
        """Ensure to_dict method creates a dict with proper attrs."""
        am = Amenity()
        new_d = am.to_dict()
        self.assertIsInstance(new_d, dict)
        self.assertNotIn("_sa_instance_state", new_d)

    def test_to_dict_values(self):
        """Check values in dict returned from to_dict are correct."""
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertIsInstance(new_d["created_at"], str)
        self.assertIsInstance(new_d["updated_at"], str)

    def test_str(self):
        """Verify correct str method output."""
        amenity = Amenity()
        expected_str = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(expected_str, str(amenity))
