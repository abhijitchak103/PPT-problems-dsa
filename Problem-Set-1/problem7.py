"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
nums = [0,1,0,3,12]
import timeit

def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    ## Method 1

    # If no elements or 1 element, then return
    # if len(nums) == 0 or len(nums) == 1:
    #     return nums
    # else:
    #     zeros = nums.count(0)

    #     for _ in range(zeros):
    #         nums.remove(0)
    #         nums.append(0)

    # return nums

    ## Method 2
    n = len(nums)
    c = 0

    for i in range(n):
        if nums[i] != 0:
            nums[c] = nums[i]
            c += 1
    
    for i in range(c, n):
        nums[i]=0

    return nums    

timeit.timeit
print(moveZeroes([0])) 
# print(timeit.timeit(moveZeroes([0])))
