import doctest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        >>> sol = Solution()
        >>> sol.strStr('hello', 'll')
        2
        >>> sol.strStr('aaaaa', 'bba')
        -1
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    doctest.testmod(verbose=True)
