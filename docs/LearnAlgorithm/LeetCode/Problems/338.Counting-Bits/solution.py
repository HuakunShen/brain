import math
from typing import List

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