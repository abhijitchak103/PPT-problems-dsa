"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]
"""

def findErrorNums(nums: list[int]) -> list[int]:
    n = len(nums)
    sum_of_nums_actual = n*(n+1)//2 
    sum_of_nums_given = sum(nums)

    nums_set = set()
    for x in nums:
        if x in nums_set:
            return [x, sum_of_nums_actual-sum_of_nums_given+x] \
                if sum_of_nums_given < sum_of_nums_actual \
                else [x, x-(sum_of_nums_given-sum_of_nums_actual)]
        nums_set.add(x)

print(findErrorNums([1,2,4,4]))        