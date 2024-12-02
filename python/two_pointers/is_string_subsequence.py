"""
392. Is Subsequence.
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be obtained 
by deleting some (or none) of the characters from the original string, 
while maintaining the relative order of the remaining characters. 

For example, "ace" is a subsequence of "abcde" while "aec" is not.
"""
import unittest

def is_sub_sequence(value: str, target: str) -> bool:
    """
    This solution uses O(1) space. The time complexity is linear with the lenght of s and t.
    """
    i = 0 # To track value string
    j = 0 # To track target sub-string
    while i < len(value) and j < len(target):
        if value[i] == target[j]:
            j += 1
        i += 1

    return j == len(target)


class TestIsSubSequence(unittest.TestCase):
    """
    Test all possible combination of Two Sum Sorted Array
    """
    def test_is_sub_sequence_success_scenario(self):
        """
        Two sum sorted success scenario test case
        """
        self.assertTrue(is_sub_sequence("abcde", "ace"))
        self.assertTrue(is_sub_sequence("abcdedfgh", "abcd"))


    def test_is_sub_sequence_failure_scenario(self):
        """
        Two sum sorted failure scenario test case
        """
        self.assertFalse(is_sub_sequence("abcdef", "xyz"))
        self.assertFalse(is_sub_sequence("abcdef", "xyzfedcba"))


if __name__ == "__main__":
    unittest.main()
