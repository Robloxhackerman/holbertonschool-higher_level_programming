#!/usr/bin/python3
"""Unittest moment"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """this will test the id attribute"""

    def setUp(self):
        self.b = Base()

    def test_1(self):
        self.assertEqual(self.b.id, 1)

    def test_2(self):
        self.assertEqual(self.b.id, 2)

    def test_3(self):
        self.assertEqual(self.b.id, 3)

class TestBase420(unittest.TestCase):
    """test for ID assignment"""

    def test_1(self):
        self.b = Base(89)
        self.assertEqual(self.b.id, 89)

class TestToJsonString(unittest.TestCase):
    """tests Base.to_json_string() method"""

    def setUp(self):
        self.b = Base()

    def test_1(self):
        self.assertEqual(self.b.to_json_string(None), "[]")

    def test_1(self):
        self.assertEqual(self.b.to_json_string([1, 2]), "[1, 2]")

class TestFromJsonString(unittest.TestCase):
    """tests Base.from_json_string"""

    def setUp(self):
        self.b = Base()

    def test_1(self):
        self.assertEqual(self.b.from_json_string(None), [])

    def test_1(self):
        self.assertEqual(self.b.from_json_string("[]"), [])

    def test_1(self):
        self.assertEqual(self.b.from_json_string('[{ "id": 89 }]'), [{'id': 89}])
