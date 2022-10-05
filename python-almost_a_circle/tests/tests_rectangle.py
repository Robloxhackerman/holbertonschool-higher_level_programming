#!/usr/bin/python3
"""Python Interpreter"""
from contextlib import redirect_stdout
import io
import unittest
from models.rectangle import Rectangle

class TestRectangle1(unittest.TestCase):
    """this will test Rectangle's capacity"""

    def test_1(self):
        """init args(1, 2)"""
        self.r = Rectangle(1, 2)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)

    def test_1b(self):
        """init args(1, 2, 3)"""
        self.r = Rectangle(1, 2, 3)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)

    def test_1c(self):
        """init args(1, 2, 3, 4)"""
        self.r = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)

    def test_1d(self):
        """init args("1", 2), etc"""
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_1e(self):
        """init args (1, 2, 3, 4, 5)"""
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)
        self.assertEqual(self.r.id, 5)

    def test_1f(self):
        """init args (-1, 2)"""
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

class TestRectangleArea(unittest.TestCase):
    """tests the area method"""

    def setUp(self):
        self.r = Rectangle(1, 2)

    def test_1(self):
        self.assertEqual(self.r.area(), 2)

    def test_01(self):
        r1 = Rectangle.save_to_file(None)
        with open("Rectangle.json") as tempFile2:
            self.assertEqual('[]', tempFile2.read())

class TestRectangleSTR(unittest.TestCase):
    """test the str method"""

    def setUp(self):
        self.r = Rectangle(1, 2, 3, 4, 5)

    def test_1(self):
        self.assertEqual(self.r.__str__(), '[Rectangle] (5) 3/4 - 1/2')

class TestRectangleDisplay(unittest.TestCase):
    """test the display method"""

    def test_0(self):
        r = Rectangle(2, 1, 0, 0)
        with io.StringIO() as test, redirect_stdout(test):
            r.display()
            output = test.getvalue()
            self.assertEqual(output, "##\n")

    def test_1(self):
        r = Rectangle(2, 1, 2, 3)
        with io.StringIO() as test, redirect_stdout(test):
            r.display()
            output = test.getvalue()
            self.assertEqual(output, "\n\n\n  ##\n")

class TestRectangleToDictonary(unittest.TestCase):
    """testss to_dict method"""

    def test_0(self):
        r = Rectangle(2, 1, 2, 3, 5)
        self.assertEqual(r.to_dictionary(), {
                         'id': 5, 'width': 2, 'height': 1, 'x': 2, 'y': 3})

class TestRectangleUpdate(unittest.TestCase):
    """tests update method"""

    def test_0(self):
        self.r = Rectangle(25, 6)
        self.r.update()
        self.assertEqual(self.r.id, 16)
        self.r.update(89)
        self.assertEqual(self.r.id, 89)
        self.r.update(89, 1)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 1)

class TestRectangleCreate(unittest.TestCase):
    """tests create method"""

    def setUp(self):
        self.r = Rectangle(25, 6)

    def test_2(self):
        self.r1 = self.r.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 1)


class TestRectangleSaveToFile(unittest.TestCase):
    """tests save to file from Rectangle"""

    def setUp(self):
        self.r = Rectangle(1, 2, 3, 4, 5)

    def test_00(self):
        r2 = Rectangle.save_to_file([])
        with open("Rectangle.json") as tempFile:
            self.assertEqual('[]', tempFile.read())

    def test_02(self):
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as temporary:
            self.assertEqual(
                '[{"id": 15, "width": 1, "height": 2, "x": 0, "y": 0}]', temporary.read())

if __name__ == '__main__':
    unittest.main()
