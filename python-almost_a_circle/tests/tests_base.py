#!/usr/bin/python3
"""unittest"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """aaaaaaa"""

    def setupinio(self):
        self.b = Base()

    def test_1(self):
        self.b = Base(89)
        self.assertEqual(self.b.id, 89)
