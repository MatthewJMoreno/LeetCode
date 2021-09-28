'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def binary_search(self, nums, target, begin_index):
        if len(nums) == 1 and nums[0] == target:
            return begin_index
        elif len(nums) == 1 and nums[0] != target:
            return -1

        mid = len(nums) // 2

        if nums[mid] == target:
            return begin_index + len(nums[:mid])

        if nums[mid] > target:
            return self.binary_search(nums[:mid], target, begin_index)

        if nums[mid] < target:
            return self.binary_search(nums[mid:], target, begin_index + len(nums[:mid]) )
        
        return -1

    def search_left_binary(self, nums, target, begin_index, last_known_index):
        print(f"nums {nums}\nbegin_index {begin_index}\nlast_known_index {last_known_index}\n")
        if len(nums) == 1 and nums[0] == target:
            return begin_index
        elif len(nums) == 1 and nums[0] != target:
            return last_known_index
        
        mid = len(nums) // 2

        #if nums[mid] == target this means we have to keep looking left
        if nums[mid] == target:
            return self.search_left_binary(nums[:mid], target, begin_index, begin_index + len(nums[:mid]))
        
        if nums[mid] < target:
            return self.search_left_binary(nums[mid:], target, begin_index + len(nums[:mid]), last_known_index)
    
    def search_right_binary(self, nums, target, begin_index, last_known_index):
        if len(nums) == 1 and nums[0] == target:
            return begin_index
        elif len(nums) == 1 and nums[0] != target:
            return last_known_index

        mid = len(nums) // 2

        #if nums[mid] == target this means we have to keep looking left
        if nums[mid] == target:
            return self.search_right_binary(nums[mid:], target, begin_index + len(nums[:mid]), begin_index + len(nums[:mid]))
        
        if nums[mid] > target:
            return self.search_left_binary(nums[:mid], target, begin_index, last_known_index)
        


    def searchRange(self, nums, target):
        first_occurance = self.binary_search(nums, target, 0)
        if first_occurance == -1:
            return [-1, -1]
        left_index = self.search_left_binary(nums[:first_occurance], target, 0, -1)
        right_index = self.search_right_binary(nums[first_occurance:], target, len(nums[:first_occurance]), -1)
        print(f"left_index {left_index}")
        print(f"right_index {right_index}")
        return first_occurance
'''

class Solution(object):
    def binary_left_search(self, nums, target, begin_index, last_known_index):
        if len(nums) == 1 and nums[0] == target:
            return begin_index
        
        if len(nums) == 1 and nums[0] != target:
            return last_known_index
        
        mid = len(nums) // 2

        if nums[mid] == target:
            last_known_index = begin_index + len(nums[:mid])
            return self.binary_left_search( nums[:mid], target, begin_index, last_known_index )
        
        if nums[mid] < target:
            return self.binary_left_search( nums[mid:], target, begin_index + len(nums[:mid]), last_known_index )

        if nums[mid] > target:
            return self.binary_left_search( nums[:mid], target,  begin_index, last_known_index)

    def binary_right_search(self, nums, target, begin_index, last_known_index):
        if len(nums) == 1 and nums[0] == target:
            return begin_index
        
        if len(nums) == 1 and nums[0] != target:
            return last_known_index
        
        mid = len(nums) // 2

        if nums[mid] == target:
            last_known_index = begin_index + len(nums[:mid])
            return self.binary_right_search( nums[mid:], target, begin_index + len(nums[:mid]), last_known_index )
        
        if nums[mid] > target:
            return self.binary_right_search( nums[:mid], target, begin_index, last_known_index )
        
        if nums[mid] < target:
            return self.binary_right_search( nums[mid:], target, begin_index + len(nums[:mid]), last_known_index )

    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        left_most_index = self.binary_left_search(nums, target, 0, -1)
        right_most_index = self.binary_right_search(nums, target, 0, -1)

        return [left_most_index, right_most_index]

test_1 = [1]
test_2 = [1,1,1,1,1,1,1]
test_3 = [2,2,3,4,4,4,4,19]
test_4 = [1,1,3,3,3,3,3,3]

sol = Solution()
print(sol.searchRange(test_4, 3))