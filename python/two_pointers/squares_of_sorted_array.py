"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
            After sorting, it becomes [0,1,9,16,100].

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
import unittest
import math


def squares_of_sorted_arr(nums: list[int]) -> list[int]:
    """
    space complexity O(n)
    time complexity O(n)
    """
    n = len(nums)
    left = 0
    right = n - 1
    result = [0] * n

    result_index = n - 1
    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]
        if left_square > right_square:
            result[result_index] = left_square
            left += 1
        else:
            result[result_index] = right_square
            right -= 1
        result_index -= 1
    return result


def squares_of_sorted_array_using_inbuilt_sorted(nums:list[int]) -> list[int]:
    """
    Using inbuilt function, first squares and then sort
    O(n) for sorting and O(n) for squaring
    """
    return sorted(math.pow(x, 2) for x in nums)

def sorted_squares_of_array(nums: list[int]) -> list[int]:
    """
    space complexity O(n)
    time complexity O(n)
    """    
    length = len(nums)
    left = 0
    right = length - 1
    result = [0] * length
    for index in range(length-1, -1, -1):
        if abs(nums[left]) > abs(nums[right]) :
            temp = nums[left]
            left += 1
        else:
            temp = nums[right]
            right -= 1
        result[index] = temp * temp
    return result


class TestSquaresOfSortedArray(unittest.TestCase):
    """
    Testcase class
    """
    def test_squares_of_sorted_array(self):
        """
        Testcase
        """
        self.assertEqual(
            sorted_squares_of_array([]),
            [])
        self.assertEqual(
            sorted_squares_of_array([2]),
            [4])
        self.assertEqual(
            sorted_squares_of_array([-4,-1,0,3,10]),
            [0,1,9,16,100])
        self.assertEqual(
            sorted_squares_of_array([-7,-3,2,3,11]),
            [4,9,9,49,121])
        self.assertEqual(
            sorted_squares_of_array([1, 2, 3, 4]),
            [1, 4, 9, 16])


if __name__ == "__main__":
    unittest.main()
