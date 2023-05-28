"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4
"""
nums = [-1,0,3,5,9,12]
target = 9

def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1

print(search(nums, target))
