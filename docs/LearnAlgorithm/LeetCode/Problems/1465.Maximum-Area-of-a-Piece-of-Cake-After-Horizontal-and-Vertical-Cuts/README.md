# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

[LeetCode Problem](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

## Solution 0

[Python Solution](./solution0.py)

[Golang Solution](./solution0.go)

**Time Complexity:** O(h*log h + v*log v + vh) for sorting

**Space Complexity:** O(v + h).

```python
from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hcuts = [0] + sorted(horizontalCuts) + [h]
        vcuts = [0] + sorted(verticalCuts) + [w]
        max_area = 0
        for i in range(len(hcuts) - 1):
            for j in range(len(vcuts) - 1):
                area = (hcuts[i + 1] - hcuts[i]) * (vcuts[j + 1] - vcuts[j])
                max_area = max(area, max_area)
        return max_area % (10**9 + 7)
```

## Solution 1

[Python Solution](./solution1.py)

**Time Complexity:** O(h*log h + v*log v) for sorting

**Space Complexity:** O(v + h).

```python
from typing import List

class Solution:
    """
    Runtime: 372 ms, faster than 7.13% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
    Memory Usage: 27.2 MB, less than 22.73% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
    """
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hcuts, vcuts = [0] + sorted(horizontalCuts) + [h], [0] + sorted(verticalCuts) + [w]
        return max(j - i for i, j in zip(hcuts, hcuts[1:])) * max(j - i for i, j in zip(vcuts, vcuts[1:])) % (10**9 + 7)
```
