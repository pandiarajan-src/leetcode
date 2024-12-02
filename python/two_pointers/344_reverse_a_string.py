"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

import unittest

def reverse_string(value: str) -> str:
    """
    Reverse a string using two pointer logic
    """
    value = list(value)
    left, right = 0, len(value) - 1
    while left < right:
        value[left], value[right] = value[right], value[left]
        left += 1
        right -= 1
    return ''.join(value)


def reverse_string_as_list(value: list[str]) -> list[str]:
    """
    in-place with O(1) extra memory
    """
    i = 0
    j = len(value) - 1
    while i < j:
        value[i], value[j] = value[j], value[i]
        i += 1
        j -= 1
    return value

class TestReverseString(unittest.TestCase):
    """Test Reverse String"""
    def test_reverse_string(self):
        """Test string reversal"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Hannah"), "hannaH")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("ab"), "ba")
        self.assertEqual(reverse_string("abc"), "cba")

    def test_reverse_string_as_list(self):
        """Test reverse string as list"""
        self.assertEqual(reverse_string_as_list(["h","e","l","l","o"]), ["o","l","l","e","h"])
        self.assertEqual(
            reverse_string_as_list(["H","a","n","n","a","h"]),
            ["h","a","n","n","a","H"]
        )
        self.assertEqual(reverse_string_as_list([]), [])
        self.assertEqual(reverse_string_as_list(["a"]), ["a"])
        self.assertEqual(reverse_string_as_list(["a", "b"]), ["b", "a"])
        self.assertEqual(reverse_string_as_list(["a", "b", "c"]), ["c", "b", "a"])

if __name__ == '__main__':
    unittest.main()
