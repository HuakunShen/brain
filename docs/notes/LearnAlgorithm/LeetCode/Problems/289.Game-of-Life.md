---
date: 2022-4-12
---
# 289. Game of Life

https://leetcode.com/problems/game-of-life/

Level: Medium (Actually Pretty Easy)

Suppose N = number of row, M = number of column

The time and space complexity are O(MN).

The entire game is played for only 1 round instead of stop when converge. So the board is traversed only for a few times.

A count board is used to store number of neighbors which has the same size as the original board.

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow, ncol = len(board), len(board[0])
        def get_num_neighbor_alive(board: List[List[int]], row: int, col: int) -> int:
            left, right = max(col - 1, 0), min(ncol, col + 2)
            top, bottom = max(0, row - 1), min(nrow, row + 2)
            count = 0
            for row_ in range(top, bottom):
                for col_ in range(left, right):
                    count += board[row_][col_]
            return count - board[row][col]
        
        
        count_board = [[0 for col in range(ncol)] for row in range(nrow)]
        for row in range(nrow):
            for col in range(ncol):
                count_board[row][col] = get_num_neighbor_alive(board, row, col)
        for row in range(nrow):
            for col in range(ncol):
                count = count_board[row][col]
                if board[row][col]:
                    # alive
                    if count < 2 or count > 3: # under-population or over-population
                        board[row][col] = 0
                else:
                    if count == 3:
                        # bring alive
                        board[row][col] = 1
```

## Short, Unreadable, Stupid, Zhuangbi Version

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow, ncol = len(board), len(board[0])
        get_num_neighbor_alive = lambda board, row, col: sum([board[r][c] for r in range(max(0, row - 1), min(nrow, row + 2)) for c in range(max(col - 1, 0), min(ncol, col + 2))]) - board[row][col]
        count_board = [[get_num_neighbor_alive(board, row, col) for col in range(ncol)] for row in range(nrow)]
        for row in range(nrow):
            for col in range(ncol):
                count = count_board[row][col]
                if board[row][col] and (count < 2 or count > 3):
                    # alive and (under-population or over-population)
                    board[row][col] = 0
                elif count == 3:
                        # bring alive
                        board[row][col] = 1
```