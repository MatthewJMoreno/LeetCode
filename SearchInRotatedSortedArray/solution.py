from typing import List

class Solution:
    def find_pivot(self, nums, begin_index, max):
        mid = len(nums) // 2

        if nums[mid] == max:
            return begin_index + len(nums[:mid])
        
        if nums[0] < nums[mid]:
            return self.find_pivot(nums[mid:], begin_index + len(nums[:mid]), max)
        else:
            return self.find_pivot(nums[:mid], begin_index, max)

    def binary_search(self, nums, target, begin_index):
        mid = len(nums) // 2

        if nums[mid] == target:
            return begin_index + len(nums[:mid])

        if nums[mid] > target:
            return self.binary_search(nums[:mid], target, begin_index)
        else:
            return self.binary_search(nums[mid:], target, begin_index + len(nums[:mid]))

    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == 1:
            return self.binary_search(nums, target, 0)
        
        pivot = self.find_pivot(nums, 0, len(nums))

        if nums[0] <= target and target <= nums[pivot]:
            return self.binary_search(nums[:pivot + 1], target, 0)
        else:
            return self.binary_search(nums[pivot + 1:], target, len(nums[:pivot]) + 1)


sol = Solution()

test_1 = [1,2,3,4,5]
test_2 = [2,3,4,5,1]
test_3 = [3,4,5,1,2]
test_4 = [4,5,1,2,3]
test_5 = [5,1,2,3,4]

test_6 = [1,2,3,4,5,6,7,8,9,10]

print(sol.search(test_2, 4))
print(sol.search(test_3, 2))
print(sol.search(test_4, 5))
print(sol.search(test_5, 1))