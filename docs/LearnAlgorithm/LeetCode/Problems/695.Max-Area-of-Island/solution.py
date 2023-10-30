from typing import List
from queue import Queue


class Solution0:
    """
    Most trivial solution with Recursion, every step is clear
    """
    def dfs(self, row: int, col: int, grid: List[List[int]], explore_map: List[List[int]]):
        if grid[row][col] == 0 or explore_map[row][col] == 1:
            return 0  # explored or empty
        area_sum = 1
        explore_map[row][col] = 1
        # search above
        if row != 0:
            area_sum += self.dfs(row - 1, col, grid, explore_map)
        # search below
        if row != len(grid) - 1:
            area_sum += self.dfs(row + 1, col, grid, explore_map)
        # search left
        if col != 0:
            area_sum += self.dfs(row, col - 1, grid, explore_map)
        # search right
        if col != len(grid[0]) - 1:
            area_sum += self.dfs(row, col + 1, grid, explore_map)
        return area_sum

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        >>> sol = Solution0()
        >>> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        >>> sol.maxAreaOfIsland(grid)
        6
        >>> grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        >>> sol.maxAreaOfIsland(grid)
        0
        """
        nrow, ncol = len(grid), len(grid[0])
        explore_map = [[0] * ncol for _ in range(nrow)]
        max_area, area_sum = 0, 0
        for row in range(nrow):
            for col in range(ncol):
                area_sum = self.dfs(row, col, grid, explore_map)
                max_area = max(max_area, area_sum)
        return max_area


class Solution1:
    """
    Same algorithm as Solution0
    Refactored and simplified some code to make it run a little faster
    Runtime: 144 ms, faster than 54.04% of Python3 online submissions for Max Area of Island.
    Memory Usage: 17 MB, less than 30.19% of Python3 online submissions for Max Area of Island.
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        >>> sol = Solution1()
        >>> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        >>> sol.maxAreaOfIsland(grid)
        6
        >>> grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        >>> sol.maxAreaOfIsland(grid)
        0
        """
        nrow, ncol = len(grid), len(grid[0])
        explore_map = [[0] * ncol for _ in range(nrow)]
        max_area, area_sum = 0, 0

        def dfs(row: int, col: int, grid: List[List[int]], explore_map: List[List[int]]):
            if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] == 0 or \
                    explore_map[row][col] == 1:
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


class Solution2:
    """
    Implement with queue, without recursion
    Runtime: 808 ms, faster than 5.03% of Python3 online submissions for Max Area of Island.
    Memory Usage: 14.7 MB, less than 82.14% of Python3 online submissions for Max Area of Island.
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        >>> sol = Solution2()
        >>> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        >>> sol.maxAreaOfIsland(grid)
        6
        >>> grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        >>> sol.maxAreaOfIsland(grid)
        0
        """
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


class Solution3:
    """
    Implement with queue (actually list), without recursion
    list was used to replace queue improve runtime by a little bit
    Runtime: 808 ms, faster than 5.03% of Python3 online submissions for Max Area of Island.
    Memory Usage: 14.7 MB, less than 82.14% of Python3 online submissions for Max Area of Island.
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        >>> sol = Solution3()
        >>> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        >>> sol.maxAreaOfIsland(grid)
        6
        >>> grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        >>> sol.maxAreaOfIsland(grid)
        0
        """
        nrow, ncol = len(grid), len(grid[0])
        seen = set()
        max_area = 0
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1 and (row, col) not in seen:
                    area_sum = 0
                    q = [(row, col)]
                    while len(q):
                        row_, col_ = q.pop()
                        if 0 <= row_ < nrow and 0 <= col_ < ncol and grid[row_][col_] == 1 and (row_, col_) not in seen:
                            seen.add((row_, col_))
                            area_sum += 1
                            q.extend([(row_ - 1, col_), (row_ + 1, col_), (row_, col_ + 1), (row_, col_ - 1)])
                    max_area = max(max_area, area_sum)
        return max_area


if __name__ == '__main__':
    import doctest

    doctest.testmod()
