"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6
"""
nums = [1,2,3]

def maximumProduct(nums: list[int]) -> int:
    nums.sort()
    return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
            

print(maximumProduct(nums))