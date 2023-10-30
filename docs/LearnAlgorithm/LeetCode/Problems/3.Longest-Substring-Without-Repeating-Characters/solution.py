import doctest


class Solution:
    """
    移动窗口
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        >>> sol = Solution()
        >>> sol.lengthOfLongestSubstring("abc")
        3
        >>> sol.lengthOfLongestSubstring("")
        0
        >>> sol.lengthOfLongestSubstring("abcabcbb")
        3
        """
        start = 0
        end = 0
        c = set()
        max_len = 0
        while end < len(s):
            char = s[end]
            if char not in c:
                c.add(s[end])
            else:
                while char in c:
                    if s[start] in c:
                        c.remove(s[start])
                    start += 1
                c.add(s[end])
            if end - start + 1 > max_len:
                max_len = end - start + 1
            end += 1
        return max_len


if __name__ == "__main__":
    doctest.testmod(verbose=True)
