# 338. Counting Bits

https://leetcode.com/problems/counting-bits/

Easy

## Topics
- Dynamic Programming
- Bit Manipulation

## Solution

```python
class Solution:
    """
        Runtime: 100 ms, faster than 75.11% of Python3 online submissions for Counting Bits.
        Memory Usage: 20.9 MB, less than 52.29% of Python3 online submissions for Counting Bits.

        Time Complexity: O(n)
        Space Complexity: O(n)
    """    
    def countBits(self, n: int) -> List[int]:
        prev_power_2 = 1
        M = [0]
        for i in range(1, n + 1):
            if math.log(i, 2) % 1 == 0:
                M.append(1)
                prev_power_2 = i
            else:
                M.append(M[prev_power_2] + M[i - prev_power_2])
        return M
```

## Explanation

The most intuitive way is to do base conversion from base 10 to base 2, then count the number of 1's, but this is too complicated to implement as a Easy question.

Since this is a dynamic programming question, we just need to find the relationship between a small number and a slightly larger number (i.e. x and x + n).

### Observations

When x is a power of 2, the number of 1's is 1.

So we can just keep track of the latest (largest) power of 2 as `prev_power_2`.

Then define `n = x - prev_power_2`.

Since `n` must be smaller than `prev_power_2` (I do it in bottom up DP), `n` must be present in the memoization table(`M`), then the number of 1's `x` has is just `M[n] + 1`.


















