import unittest
from unittest import TestCase, main
from tests import lession_1_6_10
from tests import lession_1_6_11


class MyTests(unittest.TestCase):
    def test_lastname(self):
        self.assertEqual(lession_1_6_10)
        self.assertEqual(lession_1_6_11)  # add assertion here


if __name__ == '__main__':
    unittest.main()
