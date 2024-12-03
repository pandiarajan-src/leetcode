"""
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Any subarray of size 4 is valid.
"""
from typing import List
import unittest

def find_longest_ones(bin_str: str) -> int:
    """Find the longest one"""
    left = 0
    result = 0
    curr = 0
    for right, _ in enumerate(bin_str):
        if bin_str[right] == '0':
            curr += 1
        while curr > 1:
            if bin_str[left] =='0':
                curr -= 1
            left += 1
        result = max(result, right-left+1)
    return result

def longest_ones(nums: List[int], k: int) -> int:
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    left = 0
    right = 0
    max_ones = 0
    while right < len(nums):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
        max_ones = max(max_ones, right - left + 1)
        right += 1
    return max_ones


class TestFindLongestOnes(unittest.TestCase):
    """Test Find Longest Ones"""
    def test_find_longest_ones(self):
        """test_find_longest_ones"""
        self.assertEqual(find_longest_ones("1101100111"), 5)

    def test_longest_ones(self):
        """test_longest_ones"""
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2), 6)
        self.assertEqual(longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 0), 4)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 1), 5)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 3), 10)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 4), 11)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 5), 11)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 6), 11)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 7), 11)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 8), 11)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 9), 11)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 10), 11)
        self.assertEqual(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 11), 11)


if __name__ == "__main__":
    unittest.main()
