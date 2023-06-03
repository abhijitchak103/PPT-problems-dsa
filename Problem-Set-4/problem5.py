"""
You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

**Example 1:**

$
$$
$$_

**Input:** n = 5

**Output:** 2

**Explanation:** Because the 3rd row is incomplete, we return 2
"""
n = 6
def arrangeCoins(n: int) -> int:
## Brute Force

    # i = 1
    # coins = 0
    # # required = i
    # used = 0
    # while used + i <= n:
    #     step = ["$"]*i
    #     used += len(step)
    #     coins += 1
    #     i += 1
    # return coins

## Maths
# For x filled steps, we will have total x(x+1)/2 coins as coins are in AP with 1 as CD
# for completly filled steps, we need to find x for which x(x+1)/2 = n
# Solving for x we get (sqrt(1+8*n)-1)/2
    import math
    return int(math.sqrt(1+8*n)-1)//2

print(arrangeCoins(n))
