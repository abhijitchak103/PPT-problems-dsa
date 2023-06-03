"""
Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, 
return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

**Explanation:** Only 1 and 5 appeared in the three arrays.
"""
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

## Brute Force

# arr1_2_intersect = []

# for x in arr1:
#     if x in arr2:
#         arr1_2_intersect.append(x)

# ans = []

# if len(arr1_2_intersect) == 0:
#     return []

# for x in arr1_2_intersect:
#     if x in arr3:
#         ans.append(x)

# print(ans)


def threeArrayIntersection(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    res = []
    i, j, k = 0,0,0
    p, q, r = len(arr1), len(arr2), len(arr3)
    while i < p and j < q and k < r:
        if arr1[i] == arr2[j] == arr3[k]:
            res.append(arr1[i])
            i += 1
            j += 1
            k += 1
            continue

        next_num_possible = max(arr1[i], arr2[j], arr3[k])

        if arr1[i] < next_num_possible:
            i += 1
        if arr2[j] < next_num_possible:
            j += 1
        if arr3[k] < next_num_possible:
            k += 1
    return res 

print(threeArrayIntersection(arr1, arr2, arr3))
