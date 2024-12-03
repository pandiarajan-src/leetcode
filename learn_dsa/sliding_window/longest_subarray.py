"""
Find the length of the longest subarray that has a sum less than or equal to k.
Fro example let nums = [3, 2, 1, 3, 1, 1] and k =5
"""
import unittest


def longest_subarray_length(nums, k):
    """Longest subarray length"""
    left = 0
    curr = 0
    result = 0
    for right, num in enumerate(nums):
        curr += num
        while curr > k:
            curr -= nums[left]
            left += 1
        result = max(result, right-left+1)

    return result


class TestLongestSubarrayLength(unittest.TestCase):
    """TestLongestSubarrayLength"""
    def test_example_case(self):
        """Example case"""
        nums = [3, 2, 1, 3, 1, 1]
        k = 5
        self.assertEqual(longest_subarray_length(nums, k), 3)
        nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
        k = 8
        self.assertEqual(longest_subarray_length(nums, k), 4)


    def test_empty_array(self):
        """Empty array"""
        nums = []
        k = 5
        self.assertEqual(longest_subarray_length(nums, k), 0)

    def test_all_elements_greater_than_k(self):
        """All elemetnts greater than k"""
        nums = [6, 7, 8]
        k = 5
        self.assertEqual(longest_subarray_length(nums, k), 0)

    def test_all_elements_less_than_k(self):
        """All elements less than k"""
        nums = [1, 2, 1, 1]
        k = 5
        self.assertEqual(longest_subarray_length(nums, k), 4)

    def test_single_element_equal_to_k(self):
        """Single element equal to k"""
        nums = [5]
        k = 5
        self.assertEqual(longest_subarray_length(nums, k), 1)

    def test_single_element_less_than_k(self):
        """single element less than k"""
        nums = [3]
        k = 5
        self.assertEqual(longest_subarray_length(nums, k), 1)

    def test_single_element_greater_than_k(self):
        """single element greater than k"""
        nums = [6]
        k = 5
        self.assertEqual(longest_subarray_length(nums, k), 0)

if __name__ == '__main__':
    unittest.main()
