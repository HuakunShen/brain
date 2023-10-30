# 344. Reverse String
from typing import List


class Solution:
    """
    just make a copy in the reverse direction with a for loop and
    copy the copy back using a for loop

    Success
    Runtime: 315 ms, faster than 31.20% of Python3 online submissions for Reverse String.
    Memory Usage: 18.5 MB, less than 48.52% of Python3 online submissions for Reverse String.
    """    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = [s[i] for i in range(len(s) - 1, -1, -1)]
        for i in range(len(s)):
            s[i] = tmp[i]
