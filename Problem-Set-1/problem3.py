"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2
"""

nums = [1,3,5,6]
target = 3


def searchInsert(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)

    while l <= r:
        mid = l + (r-l)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    
    return l


print(searchInsert(nums, target))