"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum(nums, target):
  complements = {}

  for i in range(len(nums)):
    if nums[i] in complements:
      return [complements[nums[i]], i]
    else:
      complements[target - nums[i]] = i


print(two_sum([3, 4, -1 , 2], 6))
print(two_sum([1, 1], 2))
print(two_sum([0, 0], 0))