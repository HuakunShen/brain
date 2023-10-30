class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Idea: for each letter, find the row it belongs to
        one round is numRows + numRows - 2 (set it to be c)
        so if idx % c == 0, then row 0
        abs(idx % c)
        """

        print(numRows)
        c = numRows * 2 - 2
        print(c)
        cycle_col = numRows - 2 + 1
        print(cycle_col)
        print(len(s) // c)
        n_cycle = len(s) // c
        n_col = n_cycle * cycle_col + max(0, len(s) % c - numRows) + 1
        print(n_col)
        grid = [[" " for c in range(n_col)] for r in range(numRows)]
        row, col = 0, 0
        offset = -1
        for i in range(len(s)):
            base_col = cycle_col * (i // c)
            x = (i + 1) - (i + 1) // numRows
            col = base_col + (x // numRows - 1) + x % numRows
            print(i, base_col, row, col)
            grid[row][col] = s[i]
            if row == numRows - 1 or row == 0:
                offset *= -1
            row += offset

        # for i in range(len(s)):
        #     row = abs(i % c)
        #     base_col = cycle_col * i // numRows
        #     col = base_col + ((i + 1) % c % numRows)
        #     print(i, row, col)
        #     grid[row][col] = s[i]
        return '\n'.join([''.join(row) for row in grid])


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAHNAPLSIIGYIR", 3))
