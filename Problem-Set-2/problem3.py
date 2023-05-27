"""
We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

Explanation: The longest harmonious subsequence is [3,2,2,2,3]
"""
nums1 = [1,3,2,2,5,2,3,7]
nums2 = [1,2,3,4]
nums3 = [1,1,1,1]


def findLHS(nums: list[int]) -> int:
    n = len(nums)

    ## Method 1

    # sub = {}
    # for i in range(n):
    #     sub[-(i+1)] = [nums[i]]
    #     sub[i+1] = [nums[i]]
    #     for j in range(i+1, n):
    #         if nums[i] - nums[j] == -1:
    #             sub[-(i+1)] += [nums[j]]
    #         elif nums[i] == nums[j]:
    #             sub[-(i+1)] += [nums[j]]
    #         elif nums[i] - nums[j] == 1:
    #             sub[i+1] += [nums[j]]
    #         elif nums[i] == nums[j]:
    #             sub[i+1] += [nums[j]]

    # max_length = 0
    # for vals in sub.values():
    #     if len(vals) > max_length and len(set(vals)) == 2 :
    #         max_length = len(vals)

    ## Method 2

    # sub = {}

    # for i in range(n):
    #     neg_target = nums[i]-1
    #     pos_target = nums[i]+1

    #     neg_count = nums.count(neg_target)
    #     pos_count = nums.count(pos_target)
    #     current_count = nums.count(nums[i])

    #     sub[-(i+1)] = [nums[i]]*current_count + [neg_target]*neg_count
    #     sub[(i+1)] = [nums[i]]*current_count + [pos_target]*pos_count

    # max_length = 0
    # for vals in sub.values():
    #     if len(vals) > max_length and len(set(vals)) == 2 :
    #         max_length = len(vals)

    # return max_length

    ## Method 3

    # dict_nums = {}

    # ans = 0

    # for i in range(n):
    #     if nums[i] in dict_nums:
    #         dict_nums[nums[i]] += [nums[i]]
    #     else:
    #         dict_nums[nums[i]] = [nums[i]]
        
    #     if nums[i]+1 in dict_nums:
    #         ans = max(ans, len(dict_nums[nums[i]]) + len(dict_nums[nums[i]+1]))
        

    #     if nums[i]-1 in dict_nums:
    #         ans = max(ans, len(dict_nums[nums[i]]) + len(dict_nums[nums[i]-1]))

    ## Method 4
    import collections
    count = collections.Counter(nums)

    ans = 0

    for x in count:
        if x+1 in count:
            ans = max(ans, count[x] + count[x+1])

    return ans

print(findLHS(nums1))