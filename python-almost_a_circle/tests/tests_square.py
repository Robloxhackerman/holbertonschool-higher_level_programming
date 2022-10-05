#!/usr/bin/python3
"""Python Interpreter"""
from contextlib import redirect_stdout
import io
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """this will test Square's capacity"""

    def test_1(self):
        """init args(1)"""
        self.s = Square(1)
        self.assertEqual(self.s.size, 1)

    def test_1b(self):
        """init args(1, 2)"""
        self.s = Square(1, 2)
        self.assertEqual(self.s.width, 1)
        self.assertEqual(self.s.height, 1)
        self.assertEqual(self.s.x, 2)

    def test_1c(self):
        """init args("1", 2), etc"""
        self.assertRaises(TypeError, Square, "1", 2)
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")

    def test_1d(self):
        self.s = Square(1, 2, 3)
        self.assertEqual(self.s.width, 1)
        self.assertEqual(self.s.height, 1)
        self.assertEqual(self.s.x, 2)
        self.assertEqual(self.s.y, 3)

    def test_1e(self):
        self.s = Square(1, 2, 3, 4)
        self.assertEqual(self.s.width, 1)
        self.assertEqual(self.s.height, 1)
        self.assertEqual(self.s.x, 2)
        self.assertEqual(self.s.y, 3)
        self.assertEqual(self.s.id, 4)

    def test_1f(self):
        """init args (-1, 2)"""
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)


class TestSquareSTR(unittest.TestCase):
    """test the str method"""

    def setUp(self):
        self.s = Square(1, 2, 3, 4)

    def test_1(self):
        self.assertEqual(self.s.__str__(), '[Square] (4) 2/3 - 1')


class TestSquareToDictonary(unittest.TestCase):
    """testss to_dict method"""

    def test_0(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.to_dictionary(), {
                         'id': 4, 'size': 1, 'x': 2, 'y': 3})


class TestSquareUpdate(unittest.TestCase):
    """tests update method"""

    def test_0(self):
        self.s = Square(25, 6)
        self.s.update()
        self.assertEqual(self.s.id, 25)
        self.s.update(89)
        self.assertEqual(self.s.id, 89)
        self.s.update(89, 1)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 1)
        self.s.update(89, 1, 2)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 1)
        self.assertEqual(self.s.x, 2)
        self.s.update(89, 1, 2, 3)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 1)
        self.assertEqual(self.s.x, 2)
        self.assertEqual(self.s.y, 3)

        self.s.update(**{ 'id': 89, 'size': 1 })
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 1)

class TestSquareCreate(unittest.TestCase):
    """tests create method"""

    def setUp(self):
        self.s = Square(25, 6)

    def test_2(self):
        self.s1 = self.s.create(**{'id': 89, 'size': 1})
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 1)


class TestSquareSaveToFile(unittest.TestCase):
    """tests save to file from Square"""

    def test_savetofilerec(self):
        Square.save_to_file(None)
        with open("Square.json") as fp:
            self.assertEqual('[]', fp.read())
        Square.save_to_file([Square(1, 2)])
        with open("Square.json") as fp3:
            self.assertEqual(
                fp3.read(), '[{"id": 24, "size": 1, "x": 2, "y": 0}]')

class TestSquareLoad(unittest.TestCase):
    """tests load"""
    def test_loadfromfilerec(self):
        Square.save_to_file([Square(1, 2)])
        lf = Square.load_from_file()
        self.assertTrue(isinstance(lf, list))

class TestMe(unittest.TestCase):
    def test_saveempty(self):
        listita = []
        Square.save_to_file(listita)
        with open("Square.json") as temp:
            self.assertEqual('[]', temp.read())

if __name__ == '__main__':
    unittest.main()
