'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''

class Solution:
    def two_sum(self, numbers, target):
        complements = {}

        for i, num in enumerate(numbers):
            complement = target - num
            if num not in complements:
                complements[complement] = i
            else:
                return [complements[num], i]

sol = Solution()
test_1 = [2,3,6,-3,10]

print(sol.two_sum(test_1, 5))
print(sol.two_sum(test_1, 8))
print(sol.two_sum(test_1, -1))
print(sol.two_sum(test_1, 13))