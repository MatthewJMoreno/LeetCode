from typing import List
import unittest

class Solution:
    def find_next_largest(self, nums, target):
      next_largest_index = -1

      for i, num in enumerate(nums):
        if target < num and next_largest_index == -1:
          next_largest_index = i
        elif target < num and num < nums[next_largest_index]:
          next_largest_index = i
      
      return next_largest_index

    def nextPermutation(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
          next_largest_index = len(nums[:i]) + 1 + self.find_next_largest( nums[i+1:], nums[i] )
          #print(f"i: {i}")
          #print(f"next_largest_index: {next_largest_index}")
          temp = nums[i]
          nums[i] = nums[next_largest_index]
          nums[next_largest_index] = temp
          #print(f"nums after swap: {nums}")
          nums[i+1:] = sorted(nums[i+1:])
          return

      nums.sort()
      return nums 

class test(unittest.TestCase):
  def test(self):
    test_1 = [1, 5, 3, 4, 2]
    test_1_expected = [1, 5, 4, 2, 3]

    test_2 = [1,3,5,4,2]
    test_2_expected = [1, 4, 2, 3, 5]

    test_3 = [5,4,3,2,1]
    test_3_expected = [1,2,3,4,5]

    test_4 = [1,2,3]
    test_4_expected = [1,3,2]

    test_5 = [3,2,1]
    test_5_expected = [1,2,3]

    test_6 = [1,1,5]
    test_6_expected = [1,5,1]

    test_7 = [1]
    test_7_expected = [1]

    sol = Solution()
    sol.nextPermutation(test_1)
    sol.nextPermutation(test_2)
    sol.nextPermutation(test_3)
    sol.nextPermutation(test_4)
    sol.nextPermutation(test_5)
    sol.nextPermutation(test_6)
    sol.nextPermutation(test_7)

    self.assertEqual(test_1, test_1_expected)
    self.assertEqual(test_2, test_2_expected)
    self.assertEqual(test_3, test_3_expected)
    self.assertEqual(test_4, test_4_expected)
    self.assertEqual(test_5, test_5_expected)
    self.assertEqual(test_6, test_6_expected)
    self.assertEqual(test_7, test_7_expected)
