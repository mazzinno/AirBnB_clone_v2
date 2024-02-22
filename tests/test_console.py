#!/usr/bin/python3
"""
Tests documentation and PEP8 compliance for the console app.
"""

import console
import pep8
import unittest
HBNBCommand = console.HBNBCommand  # Import HBNBCommand class for testing


class TestConsoleDocs(unittest.TestCase):
    """Tests for docstrings and PEP8 compliance."""

    def test_pep8_conformance_console(self):
        """Check console.py for PEP8 compliance."""
        result = pep8.StyleGuide(quiet=True).check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "console.py fails PEP8.")

    def test_pep8_conformance_test_console(self):
        """Check test_console.py for PEP8 compliance."""
        result = pep8.StyleGuide(quiet=True).check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0, "tests/test_console.py fails PEP8.")

    def test_console_module_docstring(self):
        """Ensure console.py module has a docstring."""
        self.assertTrue(console.__doc__, "Missing console.py docstring.")

    def test_HBNBCommand_class_docstring(self):
        """Check HBNBCommand class for a docstring."""
        self.assertTrue(HBNBCommand.__doc__, "Missing HBNBCommand docstring.")
