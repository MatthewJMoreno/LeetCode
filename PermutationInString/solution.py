from typing import DefaultDict
import unittest
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        s1_frequency = [0] * 26
        s2_frequency = [0] * 26

        for i, char in enumerate(s1):
            s1_frequency[ord(s1[i]) - ord('a')] += 1
            s2_frequency[ord(s2[i]) - ord('a')] += 1
        
        if s1_frequency == s2_frequency:
            return True
        
        for i in range(n, m):
            s2_frequency[ord(s2[i-n]) - ord('a')] -= 1
            s2_frequency[ord(s2[i]) - ord('a')] += 1

            if s1_frequency == s2_frequency:
                return True

        return False

class TestSolution(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        s1_test1 = 'ccab'
        s2_test1 = 'qcjcccbhzbcacf'
        test1_expected = True
        test1_actual = sol.checkInclusion(s1_test1, s2_test1)
        self.assertEqual(test1_actual, test1_expected)

        s1_test2 = 'ab'
        s2_test2 = 'eidbaooo'
        test2_expected = True
        test2_actual = sol.checkInclusion(s1_test2, s2_test2)
        self.assertEqual(test2_expected, test2_actual)

        s1_test3 = 'a'
        s2_test3 = 'bcdefghijklmnopqrstuvwxyza'
        test3_expected = True
        test3_actual = sol.checkInclusion(s1_test3, s2_test3)
        self.assertEqual(test3_expected, test3_actual)

        s1_test4 = 'cccdw'
        s2_test4 = 'aacccdjrwdcca'
        test4_expected = False
        test4_actual = sol.checkInclusion(s1_test4, s2_test4)
        self.assertEqual(test4_actual, test4_expected)

        s1_test5 = 'abc'
        s2_test5 = 'cbca'
        test5_expected = True
        test5_actual = sol.checkInclusion(s1_test5, s2_test5)
        self.assertEqual(test5_actual, test5_expected)

unittest.main()