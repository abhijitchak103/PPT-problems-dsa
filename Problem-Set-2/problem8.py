"""
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x 
where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

Example 1:
Input: nums = [1], k = 0
Output: 0

Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
"""
nums = [0,10]
k = 2

def smallestRangeI(nums: list[int], k: int) -> int:
    highest = max(nums) - k
    smallest = min(nums) + k

    diff = highest - smallest
    if diff <= 0:
        return 0
    else:
        return diff
    
print(smallestRangeI(nums, k))