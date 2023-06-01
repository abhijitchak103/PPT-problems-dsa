"""
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""
nums = [-1, 2, 1, -4]
target = 1

def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort() 

    maxsum = 10000000

    for i in range(len(nums)-2):
        p1 = i+1
        p2 = len(nums)-1

        while p1 < p2 :
            sum_now = nums[i] + nums[p1] + nums[p2]
            
            if sum_now == target:
                return sum_now
            
            if abs(target-sum_now) < abs(target-maxsum):
                maxsum = sum_now

            if sum_now < target:
                p1 += 1
            else:
                p2 -= 1
    
    return maxsum

print(threeSumClosest(nums, target))