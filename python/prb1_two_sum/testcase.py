import unittest
from solution import Solution   

class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def test_example_case(self):
        self.assertEqual(self.obj.twosum([2, 7, 11, 15], 9), [0, 1])

    def test_multiple_pairs(self):
        result = self.obj.twosum([1, 3, 4, 2], 6)
        self.assertIn(result, [[1, 2], [2, 3]])

    def test_no_solution(self):
        self.assertEqual(self.obj.twosum([1, 2, 3], 10), [])

    def test_negative_numbers(self):
        self.assertEqual(self.obj.twosum([-3, 4, 3, 90], 0), [0, 2])

    def test_duplicate_numbers(self):
        self.assertEqual(self.obj.twosum([3, 3], 6), [0, 1])

    def test_large_input(self):
        nums = list(range(1000000))
        target = 1999997
        result = self.obj.twosum(nums, target)
        self.assertEqual(nums[result[0]] + nums[result[1]], target)



if __name__ == "__main__":
    unittest.main()
