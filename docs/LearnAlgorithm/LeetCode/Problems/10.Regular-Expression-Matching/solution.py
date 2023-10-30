import doctest


class SolutionRecursion:
    """
    Runtime: 1284 ms, faster than 22.72% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 13.9 MB, less than 55.53% of Python3 online submissions for Regular Expression Matching.
    """

    def isMatch(self, s: str, p: str) -> bool:
        """
        >>> sol = SolutionRecursion()
        >>> print(sol.isMatch("aa", "a"))
        False
        >>> print(sol.isMatch("aa", "a*"))
        True
        >>> print(sol.isMatch("ab", ".*"))
        True
        >>> print(sol.isMatch("aab", "c*a*b"))
        True
        >>> print(sol.isMatch("mississippi", "mis*is*p*."))
        False
        >>> print(sol.isMatch("aaa", "a*a"))
        True
        >>> print(sol.isMatch("bbbba", ".*a*a"))
        True
        """
        if len(p) == 0:
            return len(s) == 0
        first_char_match = s and (s[0] == p[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_char_match and self.isMatch(s[1:], p))
        else:
            return first_char_match and self.isMatch(s[1:], p[1:])


class SolutionDP1:
    """
    Runtime: 36 ms, faster than 97.64% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14.1 MB, less than 10.73% of Python3 online submissions for Regular Expression Matching.
    """

    def isMatch(self, s: str, p: str) -> bool:
        """
        >>> sol = SolutionDP1()
        >>> print(sol.isMatch("aa", "a"))
        False
        >>> print(sol.isMatch("aa", "a*"))
        True
        >>> print(sol.isMatch("ab", ".*"))
        True
        >>> print(sol.isMatch("aab", "c*a*b"))
        True
        >>> print(sol.isMatch("mississippi", "mis*is*p*."))
        False
        >>> print(sol.isMatch("aaa", "a*a"))
        True
        >>> print(sol.isMatch("bbbba", ".*a*a"))
        True
        >>> print(sol.isMatch("ab", ".*c"))
        False
        """
        memo = {}

        def dp(row, col):
            if not (row, col) in memo:
                if col == len(p):
                    ans = row == len(s)
                else:
                    first_match = row < len(s) and p[col] in {s[row], '.'}
                    if col + 1 < len(p) and p[col + 1] == '*':
                        ans = (first_match and dp(row + 1, col)) or dp(row, col + 2)
                    else:
                        ans = first_match and dp(row + 1, col + 1)
                memo[(row, col)] = ans
            return memo[(row, col)]

        return dp(0, 0)


class SolutionDP2:
    """
    Runtime: 2912 ms, faster than 5.05% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14 MB, less than 21.16% of Python3 online submissions for Regular Expression Matching.
    """

    def isMatch(self, s: str, p: str) -> bool:
        """
        >>> sol = SolutionDP2()
        >>> print(sol.isMatch("aa", "a"))
        False
        >>> print(sol.isMatch("aa", "a*"))
        True
        >>> print(sol.isMatch("ab", ".*"))
        True
        >>> print(sol.isMatch("aab", "c*a*b"))
        True
        >>> print(sol.isMatch("mississippi", "mis*is*p*."))
        False
        >>> print(sol.isMatch("aaa", "a*a"))
        True
        >>> print(sol.isMatch("bbbba", ".*a*a"))
        True
        >>> print(sol.isMatch("ab", ".*c"))
        False
        """
        memo = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        def dp(row, col):
            if not memo[row][col]:
                if col == len(p):
                    ans = row == len(s)
                else:
                    first_match = row < len(s) and p[col] in {s[row], '.'}
                    if col + 1 < len(p) and p[col + 1] == '*':
                        ans = (first_match and dp(row + 1, col)) or dp(row, col + 2)
                    else:
                        ans = first_match and dp(row + 1, col + 1)
                memo[row][col] = ans
            return memo[row][col]

        return dp(0, 0)


class SolutionDPBottomUp1:
    """
    Runtime: 48 ms, faster than 82.23% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14.1 MB, less than 16.86% of Python3 online submissions for Regular Expression Matching.
    """

    def isMatch(self, s: str, p: str) -> bool:
        """
        >>> sol = SolutionDPBottomUp1()
        >>> print(sol.isMatch("aa", "a"))
        False
        >>> print(sol.isMatch("aa", "a*"))
        True
        >>> print(sol.isMatch("ab", ".*"))
        True
        >>> print(sol.isMatch("aab", "c*a*b"))
        True
        >>> print(sol.isMatch("mississippi", "mis*is*p*."))
        False
        >>> print(sol.isMatch("aaa", "a*a"))
        True
        >>> print(sol.isMatch("bbbba", ".*a*a"))
        True
        >>> print(sol.isMatch("ab", ".*c"))
        False
        """
        memo = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        memo[-1][-1] = True
        for row in range(len(s), -1, -1):
            for col in range(len(p) - 1, -1, -1):
                first_match = row < len(s) and p[col] in {s[row], '.'}
                if col + 1 < len(p) and p[col + 1] == '*':
                    memo[row][col] = (first_match and memo[row + 1][col]) or memo[row][col + 2]
                else:
                    memo[row][col] = first_match and memo[row + 1][col + 1]

        return memo[0][0]


class SolutionDPBottomUp2:
    """
    Runtime: 40 ms, faster than 94.16% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14 MB, less than 26.04% of Python3 online submissions for Regular Expression Matching.
    """

    def isMatch(self, s: str, p: str) -> bool:
        """
        >>> sol = SolutionDPBottomUp2()
        >>> print(sol.isMatch("aa", "a"))
        False
        >>> print(sol.isMatch("aa", "a*"))
        True
        >>> print(sol.isMatch("ab", ".*"))
        True
        >>> print(sol.isMatch("aab", "c*a*b"))
        True
        >>> print(sol.isMatch("mississippi", "mis*is*p*."))
        False
        >>> print(sol.isMatch("aaa", "a*a"))
        True
        >>> print(sol.isMatch("bbbba", ".*a*a"))
        True
        >>> print(sol.isMatch("ab", ".*c"))
        False
        >>> print(sol.isMatch("a", ".*..a*"))
        False
        """
        memo = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        memo[0][0] = True
        for col in range(1, len(memo[0])):
            if p[col - 1] == "*":
                memo[0][col] = memo[0][col - 2]
        for row in range(1, len(memo)):
            for col in range(1, len(memo[0])):
                cur_p, cur_s = p[col - 1], s[row - 1]
                first_match = cur_p in {cur_s, '.'}
                if first_match:
                    # check previous pattern and string char
                    memo[row][col] = memo[row - 1][col - 1]
                elif cur_p == '*':
                    # case 1: 0 occurrence for *, then check 2 pattern char before, col - 2
                    # case 2: repeat char, then check previous string char. If current repeating pattern matches current string char.
                    memo[row][col] = memo[row][col - 2] or (p[col - 2] in {cur_s, '.'} and memo[row - 1][col])
                else:
                    # doesn't match
                    memo[row][col] = False
        for row in memo:
            print(row)
        return memo[len(s)][len(p)]


if __name__ == "__main__":
    # doctest.testmod()
    sol = SolutionDPBottomUp2()
    print(sol.isMatch("aa", "a*"))

