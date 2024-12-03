"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k 
    that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000

Constraints:
    n == nums.length
    1 <= k <= n <= 104
    -104 <= nums[i] <= 104

"""

import unittest

def find_max_average(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    left = 0
    right = k
    curr = 0
    for index in range(left, right):
        curr += nums[index]
    # Take average of the first subarray consider it as answer
    answer = curr
    for index in range(right, len(nums)):
        curr = curr - nums[index-k] + nums[index]
        answer = max(answer, curr)
    return answer/k

class TestFindMaxAverage(unittest.TestCase):
    """Test for find_max_average function"""
    def test_avg_subarray(self):
        """Test for find_max_average function"""
        self.assertAlmostEqual(find_max_average([1, 12, -5, -6, 50, 3], 4), 12.75, places=5)
        self.assertAlmostEqual(find_max_average([5], 1), 5.0, places=5)
        self.assertAlmostEqual(find_max_average([0, 4, 0, 3, 2], 1), 4.0, places=5)
        self.assertAlmostEqual(find_max_average([0, 4, 0, 3, 2], 4), 2.25, places=5)
        self.assertAlmostEqual(find_max_average([0, 4, 0, 3, 2], 5), 1.8, places=5)

if __name__ == "__main__":
    unittest.main()
