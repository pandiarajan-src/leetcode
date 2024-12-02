"""
Two pointer simple example of Polindrom
"""

import unittest

def is_polindrome(val : str) -> bool:
    """
    Check whether the given stirng is polindrom, if so return True else False
    This algorithm is very efficient as not only does it run in O(n), 
    but it also uses only O(1) space.
    """
    i = 0
    j = len(val) - 1

    while i < j:
        if val[i] != val[j]:
            return False
        i += 1
        j -= 1
    return True


class TestIsPolindromeMethod(unittest.TestCase):
    """
    Test all the possible combination of polindrome success and failure cases.
    """
    def test_is_polindrome_success_scenarios(self):
        """
        Test success scenarios of polindrome
        """
        test_success_inputs = ['racecar', 'abcdcba']
        for s_input in test_success_inputs:
            self.assertTrue(is_polindrome(s_input))

    def test_is_polindrome_failure_scenarios(self):
        """
        Test failure scenarios of polindrome
        """
        test_failure_inputs = ['abcdefh', 'howarehow']
        for f_input in test_failure_inputs:
            self.assertFalse(is_polindrome(f_input))


if __name__ == "__main__":
    unittest.main()
