import doctest
from functools import lru_cache

import numpy as np


# Brute Force (Time Limit Exceeded)
class Solution0:
    def longestValidParentheses(self, s: str) -> int:
        """
        >>> sol = Solution1()
        >>> sol.longestValidParentheses("(()")
        2
        >>> sol.longestValidParentheses(")()())")
        4
        >>> sol.longestValidParentheses("")
        0
        >>> sol.longestValidParentheses(")(")
        0
        >>> sol.longestValidParentheses("()(()")
        2
        >>> sol.longestValidParentheses("()()")
        4
        """

        def is_valid(s_):
            open_count = 0
            for c in s_:
                if c == '(':
                    open_count += 1
                else:
                    if open_count > 0:
                        open_count -= 1
                    else:
                        return False
            return open_count == 0

        l = len(s)
        dp_table = [[0] * l for _ in range(l)]
        max_l = 0
        for i in range(l):
            for j in range(i, l):
                if is_valid(s[i:j + 1]):
                    dp_table[i][j] = j - i + 1
                    max_l = max(max_l, dp_table[i][j])
        return max_l


# Dynamic Programming
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        """
        >>> sol = Solution1()
        >>> sol.longestValidParentheses("(()")
        2
        >>> sol.longestValidParentheses(")()())")
        4
        >>> sol.longestValidParentheses("")
        0
        >>> sol.longestValidParentheses(")(")
        0
        >>> sol.longestValidParentheses("()(()")
        2
        >>> sol.longestValidParentheses("()()")
        4
        """
        table = [-3] * len(s)

        def dp_table(i):
            if i == -1:
                return 0
            if table[i] == -3:
                table[i] = dp(i)
            return table[i]

        def dp(i):
            if s[i] == "(": return 0
            if i >= 1 and s[i - 1:i + 1] == "()": return dp_table(i - 2) + 2
            P = i - dp_table(i - 1) - 1
            if P >= 0 and s[P] == "(":
                return dp_table(i - 1) + dp_table(P - 1) + 2
            return 0

        return max(dp_table(i) for i in range(len(s))) if s else 0


if __name__ == '__main__':
    doctest.testmod()
