# 474. Ones and Zeroes

[Python Solution](./solution.py)

Time Complexity: $O(m\cdot n\cdot len(strs))$

Space Complexity: $O(m\cdot n)$

## Dynamic Programming (Bottom Up)

Each string in `strs` can be either in or not in the solution set.

The other interpretation of the algorithm is actually finding out whether a string should be in the solution set.

If a string `s` is added to the solution set, x 0's and y 1's are added. If we look back at the case where `s` isn’t
added yet, we know the maximum solution set size for the subproblem ($m_{sub}=m-num\_zeros, n_{sub}=n-num\_ones$),
adding a one to it gives us the solution set for current case, but if current cell already has a larger value, we should
skip this case. We can do this with a $max$ function.

### Bellman Equation:

$DP[i, j] = max(DP[i, j], DP[i - num\_zeros, j - num\_ones])$

```python
import numpy as np
from typing import List


class Solution:
    """
    Numpy Version
    """

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp_table = np.zeros((m + 1, n + 1)).astype(int)
        for s in strs:
            num_zeros = s.count("0")
            num_ones = len(s) - num_zeros
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= num_zeros and j >= num_ones:
                        dp_table[i, j] = max(dp_table[i - num_zeros, j - num_ones] + 1, dp_table[i, j])
        return dp_table[m, n]


if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m, n = 5, 3
    sol = Solution()
    print(sol.findMaxForm(strs, m, n))
```

In the example above (in main),

| index | 0    | 1    | 2    | 3                |
| ----- | ---- | ---- | ---- | ---------------- |
| **0** | 0    | 1    | 1    | 1                |
| **1** | 1    | 2    | 2    | 2                |
| **2** | 1    | 2    | 3    | 3                |
| **3** | 1    | 2    | 3    | 3                |
| **4** | 1    | 2    | 3    | 3                |
| **5** | 1    | 2    | 3    | **4 (solution)** |

### Note

The 2 inner for loops doesn't start from 0, but from m and n. 

This is because larger values depend on smaller values (sub-problems)

If the 2 inner loops starts from 0, a string could be double counted.

### Update

An updated version of the code to save a little of runtime:

```python
def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    dp_table = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        num_zeros = s.count("0")
        num_ones = len(s) - num_zeros
        for i in range(m, num_zeros - 1, -1):
            for j in range(n, num_ones - 1, -1):
                dp_table[i][j] = max(dp_table[i - num_zeros][j - num_ones] + 1, dp_table[i][j])
    return dp_table[m][n]
```























