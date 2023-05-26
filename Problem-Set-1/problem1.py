"""
**Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]
"""

nums = [6, 7, 2, 11]
target = 9

def get_indices(nums: list[int], target: int) -> list[int]:
    # for i in range(len(nums)):
        ## Method 1

        # for j in range(i+1, len(nums)):
        #     if nums[i] + nums[j] == target:
        #         return [i, j]

        ## Method 2

        # diff = target - nums[i]
        # nums_to_loop = nums[i+1:]
        # if diff in nums_to_loop:
        #     return [i, nums_to_loop.index(diff)+i+1]
        
    ## Method 3
    temp = {}    
    for i, x in enumerate(nums):

        if x in temp:
            return [i, temp[x]]

        temp[target - x] = i

print(get_indices(nums, target))