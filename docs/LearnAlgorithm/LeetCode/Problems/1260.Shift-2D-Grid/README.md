# 1260. Shift 2D Grid

https://leetcode.com/problems/shift-2d-grid/

Level: Easy

Python should be the easiest to solve this problem with some string and list manipulation syntactic sugar.

Given that a matrix contains n elements in total.

**Time Complexity**: O(n), every step takes O(n) of time.

**Space Complexity**: O(n), space for storing result and intermediate result. O(1) space for storing other variables.




```python
class Solution:
    """
    Runtime: 193 ms, faster than 70.75% of Python3 online submissions for Shift 2D Grid.
    Memory Usage: 14.4 MB, less than 35.10% of Python3 online submissions for Shift 2D Grid.
    """
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nrow, ncol = len(grid), len(grid[0])
        flat_grid = [ele for row in grid for ele in row]        # O(n)
        grid_size = len(flat_grid)
        k = k % grid_size
        part1 = flat_grid[:(grid_size-k)]                       # O(n)
        part2 = flat_grid[(grid_size-k):]                       # O(n)
        part2.extend(part1)                                     # O(n)
        return [part2[i*ncol:(i+1)*ncol] for i in range(nrow)]  # O(n)
```