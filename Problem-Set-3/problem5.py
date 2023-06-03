"""
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

digits = [1,2,3]

def plusOne(digits: list[int]) -> list[int]:
    n = len(digits)
    num = 0
    for i in range(n):
        power = n - i - 1
        num += digits[i]*10**power

    num += 1

    return [int(x) for x in str(num)]

print(plusOne(digits))