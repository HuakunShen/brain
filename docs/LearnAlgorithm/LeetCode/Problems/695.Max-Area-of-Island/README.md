# 695. Max Area of Island

[LeetCode](https://leetcode.com/problems/max-area-of-island/)

[Python Solution](./solution.py)

## DFS Recursive

**Time Complexity:** O(R x C)

**Space Complexity:** O(R x C)

Where R = num row and C = num col

```python
from typing import List


class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        explore_map = [[0] * ncol for _ in range(nrow)]
        max_area, area_sum = 0, 0

        def dfs(row: int, col: int, grid: List[List[int]], explore_map: List[List[int]]):
            if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] == 0 or explore_map[row][col] == 1:
                return 0  # explored or empty
            explore_map[row][col] = 1
            # search above
            return 1 + dfs(row - 1, col, grid, explore_map) + dfs(row + 1, col, grid, explore_map) + dfs(
                row, col - 1, grid, explore_map) + dfs(row, col + 1, grid, explore_map)

        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1 and explore_map[row][col] == 0:
                    area_sum = dfs(row, col, grid, explore_map)
                    max_area = max(max_area, area_sum)
        return max_area
```

## DFS Iterative

**Time Complexity:** O(R x C)

**Space Complexity:** O(R x C)

Where R = num row and C = num col

```python
from typing import List
from queue import Queue


class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        seen = set()
        max_area = 0
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1 and (row, col) not in seen:
                    area_sum = 0
                    q = Queue()
                    q.put((row, col))
                    while not q.empty():
                        row_, col_ = q.get()
                        if 0 <= row_ < nrow and 0 <= col_ < ncol and grid[row_][col_] == 1 and (row_, col_) not in seen:
                            seen.add((row_, col_))
                            area_sum += 1
                            q.put((row_ - 1, col_))
                            q.put((row_ + 1, col_))
                            q.put((row_, col_ + 1))
                            q.put((row_, col_ - 1))
                    max_area = max(max_area, area_sum)
        return max_area
```