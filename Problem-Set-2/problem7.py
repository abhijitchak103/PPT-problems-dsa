"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true
"""

nums = [1,2,2,3]

def isMonotonic(nums: list[int]) -> bool:
    if len(nums) == 0 or len(nums) == 1:
        return True
    else:
        high = max(nums)
        low = min(nums)

        if nums[0] == low and nums[-1] == high:
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True
        elif nums[0] == high and nums[-1] == low:
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    return False
            return True
        else:
            return False
        
print(isMonotonic(nums))