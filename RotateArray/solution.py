'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
do not return anything, rotate the array in place
'''

class Solution():
    def rotate(self, nums, k):
        k = k % len(nums)
        pivot_index = len(nums) - k
        nums[:pivot_index] = reversed(nums[:pivot_index])
        nums[pivot_index:] = reversed(nums[pivot_index:])
        nums[:] = reversed(nums[:])
        print(nums)

test_arr = [1,2]

sol = Solution()
sol.rotate([1,2],1)
sol.rotate([1,2],2)
sol.rotate([1,2],3)
sol.rotate([1,2],4)
sol.rotate([1,2],5)
