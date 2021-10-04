'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def binary_search(self, nums, target, begin_index):
        if len(nums) == 1 and nums[0] < target:
            return begin_index + 1
        
        if len(nums) == 1 and nums[0] > target:
            if begin_index - 1 < 0:
                return 0
            return begin_index - 1
        
        if len(nums) == 1 and nums[0] == target:
            return begin_index
        
        mid = len(nums) // 2

        if nums[mid] == target:
            return begin_index + len(nums[:mid])
        elif nums[mid] < target:
            return self.binary_search(nums[mid:], target, begin_index + len(nums[:mid]))
        else:
            return self.binary_search(nums[:mid], target, begin_index)


    def searchInsert(self, nums, target):
        return self.binary_search(nums, target, 0)

sol = Solution()
test_arr_1 = [1]
test_arr_2 = [1,2,3,6,7,10]

#print(sol.searchInsert(test_arr_1, 0))
#print(sol.searchInsert(test_arr_1, 1))
#print(sol.searchInsert(test_arr_1, 4))
print()
print(sol.searchInsert(test_arr_2, 2))
print(sol.searchInsert(test_arr_2, 5))
print(sol.searchInsert(test_arr_2, 8))
print(sol.searchInsert(test_arr_2, 20))
