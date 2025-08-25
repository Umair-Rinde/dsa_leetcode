import unittest
from solution import Solution

class TestSubstring(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def test_empty_string(self):
        self.assertEqual(self.obj.substring(""), 0)

    def test_single_char(self):
        self.assertEqual(self.obj.substring("a"), 1)

    def test_all_unique(self):
        self.assertEqual(self.obj.substring("abcdef"), 6)

    def test_repeated_chars(self):
        self.assertEqual(self.obj.substring("abcabcbb"), 3)  # "abc"

    def test_all_same_char(self):
        self.assertEqual(self.obj.substring("bbbbbb"), 1)

    def test_mix_chars(self):
        self.assertEqual(self.obj.substring("pwwkew"), 3)  # "wke"

    def test_with_spaces(self):
        self.assertEqual(self.obj.substring("a b c a b"), 3)  # "a b" or "b c"

    def test_long_input(self):
        s = "abcdefghijklmnopqrstuvwxyz" * 10
        self.assertEqual(self.obj.substring(s), 26)


if __name__ == "__main__":
    unittest.main()
