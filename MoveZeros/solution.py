class Solution:
    def moveZeros(self, nums):
        last_non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0
        
sol = Solution()
test_1 = [-3, 10, -5, 0, 0, 3]
sol.moveZeros(test_1)
print(test_1)