"""
Given a sorted array of unique integers and a target integer, 
return true if there exists a pair of numbers that sum to target, 
        false otherwise. 

This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, 
return true because 4 + 9 = 13.
"""
import unittest

def two_sum_sorted_array(nums : list[int], target: int) -> bool:
    """
    Assume the given input nums is sorted array
    This algorithm uses O(1) space and has a time complexity of O(n)
    """
    i = 0
    j = len(nums) - 1

    while i < j:
        sum_val = nums[i] + nums[j]
        if sum_val == target:
            return True
        if sum_val > target:
            j -= 1
        else:
            i += 1
    return False


class TestTwoSumSortedArray(unittest.TestCase):
    """
    Test all possible combination of Two Sum Sorted Array
    """
    def test_two_sum_sorted_success_scenario(self):
        """
        Two sum sorted success scenario test case
        """
        self.assertTrue(two_sum_sorted_array([1, 2, 4, 6, 8, 9, 14, 15], 13))

    def test_two_sum_sorted_failure_scenario(self):
        """
        Two sum sorted failure scenario test case
        """
        self.assertFalse(two_sum_sorted_array([1, 2, 3, 4, 5, 6], 13))

if __name__ == "__main__":
    unittest.main()
