import unittest
from functions import add


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 2), 12)
        self.assertEqual(add(4, 2), 6)
        self.assertNotEqual(add(4, 2), 8)

    def test_add_2(self):
        self.assertEqual(add(10, 2), 12)
        self.assertEqual(add(4, 2), 6)
        self.assertNotEqual(add(4, 2), 8)


if __name__ == '__main__':
    unittest.main()
