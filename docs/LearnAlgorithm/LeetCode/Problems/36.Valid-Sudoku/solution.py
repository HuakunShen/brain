# 36. Valid Sudoku
import doctest
from typing import List, Dict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for row in board:
            if not self.valid_row(row):
                return False
        # column check
        for col_index in range(len(board)):
            row = [board[row_index][col_index] for row_index in range(len(board[col_index]))]
            if not self.valid_row(row):
                return False

        # square check
        for row in range(3):
            for col in range(3):
                nums = []
                for i in range(3):
                    for j in range(3):
                        nums.append(board[row * 3 + i][col * 3 + j])
                if not self.valid_row(nums):
                    return False
        return True

    def valid_row(self, lst) -> bool:
        s = set()
        try:
            for element in lst:
                if element != '.':
                    if 9 >= int(element) >= 1:
                        old_size = len(s)
                        s.add(element)
                        if old_size == len(s):
                            return False
                    else:
                        return False
        except ValueError:
            return False
        return True


if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    sol = Solution()
    test_input = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    assert sol.isValidSudoku(test_input) is True

    test_input = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    assert sol.isValidSudoku(test_input) is False

    test_input = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    assert sol.isValidSudoku(test_input) is False
