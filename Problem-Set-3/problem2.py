"""
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""
nums = [1,0,-1,0,-2,2]
target = 0

def fourSum(nums: list[int], target: int) -> list[list[int]]:
    quarts = set()
    summap = dict()
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            twosum = nums[i] + nums[j]

            if twosum not in summap:
                summap[twosum] = [(i, j)]
            else:
                summap[twosum] += [(i,j)]

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            rem = target - nums[i]-nums[j]

            if rem in summap:
                pairs = summap[rem]

                for pair in pairs:
                    if pair[0] != i and pair[0] != j and pair[-1] != i and pair[-1] != j:
                        element = [nums[pair[0]], nums[pair[1]], nums[i], nums[j]]
                        element.sort()
                        quarts.add(tuple(element))
    
    return [list(x) for x in quarts]

print(fourSum(nums, target))

