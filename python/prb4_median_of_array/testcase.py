import unittest
from solution import Solution

class TestMedianOfArray(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def test_both_empty(self):
        with self.assertRaises(ZeroDivisionError):  
            self.obj.medianOfArray([], [])

    def test_one_empty(self):
        self.assertEqual(self.obj.medianOfArray([1, 2, 3], []), 2.0)

    def test_even_length(self):
        self.assertEqual(self.obj.medianOfArray([1, 3], [2, 4]), 2.5)

    def test_odd_length(self):
        self.assertEqual(self.obj.medianOfArray([1, 2], [3]), 2.0)

    def test_unsorted_inputs(self):
        self.assertEqual(self.obj.medianOfArray([3, 1], [4, 2]), 2.5)

    def test_negative_numbers(self):
        self.assertEqual(self.obj.medianOfArray([-3, -1], [-2, -4]), -2.5)

    def test_large_numbers(self):
        self.assertEqual(self.obj.medianOfArray([1000000], [1000001]), 1000000.5)

    def test_duplicates(self):
        self.assertEqual(self.obj.medianOfArray([1, 2, 2], [2, 3]), 2.0)


if __name__ == "__main__":
    unittest.main()
