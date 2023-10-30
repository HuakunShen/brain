from typing import List


class Solution:
    """
    Runtime: 372 ms, faster than 7.13% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
    Memory Usage: 27.2 MB, less than 22.73% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
    """
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hcuts, vcuts = [0] + sorted(horizontalCuts) + [h], [0] + sorted(verticalCuts) + [w]
        return max(j - i for i, j in zip(hcuts, hcuts[1:])) * max(j - i for i, j in zip(vcuts, vcuts[1:])) % (10**9 + 7)