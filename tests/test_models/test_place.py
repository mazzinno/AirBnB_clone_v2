#!/usr/bin/python3
"""Unit tests for the Place class."""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(test_basemodel):
    """Test cases for the Place class."""

    def setUp(self):
        """Set up test instances."""
        super().setUp()
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test type of city_id attribute."""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test type of user_id attribute."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test type of name attribute."""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test type of description attribute."""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test type of number_rooms attribute."""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test type of number_bathrooms attribute."""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Test type of max_guest attribute."""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test type of price_by_night attribute."""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test type of latitude attribute."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test type of longitude attribute."""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Test type of amenity_ids attribute."""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
