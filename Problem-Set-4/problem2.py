"""
Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]

**Output:** [[1,3],[4,6]]

**Explanation:**

For nums1, nums1[1] = 2 is present at index 0 of nums2, 
whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. 
Therefore, answer[0] = [1,3].

For nums2, nums2[0] = 2 is present at index 1 of nums1, 
whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. 
Therefore, answer[1] = [4,6].
"""
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:

    nums1 = list(set(nums1))
    # Doing this to make sure the lists are sorted.
    nums1.sort()
    nums2 = list(set(nums2))
    # Doing this to make sure the lists are sorted.
    nums2.sort()
    i, j = 0, 0
    p, q = len(nums1), len(nums2)
    nums1_arr = []
    nums2_arr = []
    while i < p and j < q:
        if nums1[i] == nums2[j]:
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            nums1_arr.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1

    if i <= p-1:
        nums1_arr.extend(nums1[i:])

    i, j = 0, 0
    while i < p and j < q:
        if nums1[i] == nums2[j]:
            i += 1
            j += 1
        elif nums2[j] < nums1[i]:
            nums2_arr.append(nums2[j])
            j += 1
        elif nums2[j] > nums1[i]:
            i += 1
    
    if j <= q-1:
        nums2_arr.extend(nums2[j:])
    
    res = [nums1_arr, nums2_arr]

    return res

print(findDifference(nums1, nums2))