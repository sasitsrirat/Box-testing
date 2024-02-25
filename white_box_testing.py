# white_box_testing.py
import unittest

def add(x, y):
    return y + y

class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_negative_numbers(self):
        result = add(-3, -5)
        self.assertEqual(result, -8)

    def test_mixed_numbers(self):
        result = add(2, -5)
        self.assertEqual(result, -3)

if __name__ == '__main__':
    unittest.main()