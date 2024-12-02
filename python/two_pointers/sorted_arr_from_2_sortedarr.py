"""
Given two sorted integer arrays arr1 and arr2, 
return a new array that combines both of them and is also sorted.
"""
import unittest

def sort_array_from_2_sortedarray(nums1 : list[int], nums2 : list [int]) -> list[int]:
    """
    this algorithm has a time complexity of O(n) and uses O(1) space
    (if we don't count the output as extra space, which we usually don't).
    """
    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    while i < len(nums1):
        result.append(nums1[i])
        i += 1

    while j < len(nums2):
        result.append(nums2[j])
        j += 1

    return result

class TestSortedArrayFrom2SortedArrays(unittest.TestCase):
    """
    Test all the possible combination scenarios for TestSortedArrayFrom2SortedArrays
    """
    def test_sort_array_from_2_sortedarray_scenario(self):
        """
        success
        """
        self.assertEqual(
            sort_array_from_2_sortedarray([1, 4, 7, 20], [3, 5, 6]),
            [1, 3, 4, 5, 6, 7, 20])
        self.assertEqual(
            sort_array_from_2_sortedarray([1, 3, 5, 7], [2, 4, 6, 7, 8]),
            [1, 2, 3, 4, 5, 6, 7, 7, 8])
        self.assertEqual(
            sort_array_from_2_sortedarray([1, 2, 3, 4, 5, 7], [12, 14, 16, 17, 18]),
            [1, 2, 3, 4, 5, 7, 12, 14, 16, 17, 18])

if __name__ == "__main__":
    unittest.main()
