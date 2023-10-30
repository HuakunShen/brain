# 20. Valid Parentheses
import doctest


class Solution:
    def isValid(self, s: str) -> bool:
        """
        >>> sol = Solution()
        >>> sol.isValid('()')
        True
        >>> sol.isValid('()[]{}')
        True
        >>> sol.isValid('(]')
        False
        >>> sol.isValid('([)]')
        False
        >>> sol.isValid('{[]}')
        True
        """
        dict = {
            '{': '}',
            '}': '{',
            '(': ')',
            ')': '(',
            '[': ']',
            ']': '['
        }
        stack = []
        for i in range(len(s)):
            if stack:
                if dict[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

            if len(stack) > len(s) - i - 1:
                return False
        if not stack:
            return True


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    # sol = Solution()
    # print(sol.isValid('()'))
    # print(sol.isValid('()[]{}'))
    # print(sol.isValid('(]'))
    # print(sol.isValid('([)]'))
    # print(sol.isValid('{[]}'))
    # print(sol.isValid('){'))
