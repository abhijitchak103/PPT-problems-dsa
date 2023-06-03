"""
Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]
"""
nums = [-4,-1,0,3,10]

def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(x**2 for x in nums)
# Method 1
    # l,r = 0, len(nums)-1
    # squares = []
    # while l < r:
    #     if nums[l]**2 < nums[r]**2:
    #         squares.append(nums[r]**2)
    #         r -= 1
    #     elif nums[l]**2 > nums[r]**2:
    #         squares.append(nums[l]**2)
    #         l += 1
    # squares.append(nums[l]**2)

    # squares = reverse(squares)    
    # return squares

# def reverse(nums: list[int]) -> list[int]:
#     l, r = 0, len(nums)-1
#     while l < r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1
#     return nums


print(sortedSquares(nums))