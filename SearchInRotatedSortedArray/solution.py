from typing import List

class Solution:
    def find_pivot(self, nums, begin_index, max):
        print(nums)
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
        pivot = self.find_pivot(nums, 0, len(nums))

        if nums[0] <= target and target <= nums[pivot]:
            return self.binary_search(nums[:pivot + 1], target, 0)
        else:
            return self.binary_search(nums[pivot + 1:], target, len(nums[:pivot]) + 1)


sol = Solution()

test_1 = [-1, 0, 1, 2, 3, 4, -3, -2]

target_1 = 2
target_2 = 4
target_3 = -3

print(sol.search(test_1, target_1))