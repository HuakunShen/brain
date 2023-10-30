import doctest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        >>> sol = Solution()
        >>> sol.longestPalindrome('bb')
        'bb'
        >>> sol.longestPalindrome('babad')
        'bab'
        >>> sol.longestPalindrome('cbba')
        'bb'
        >>> sol.longestPalindrome('qabbap')
        'abba'
        """
        longest = ''
        # find odd palindrome
        for i in range(len(s)):
            j = 0
            while i - j >= 0 and i + j < len(s):
                if s[i - j] == s[i + j]:
                    if 2 * j + 1 > len(longest):
                        longest = s[i - j:i + j + 1]
                    j += 1
                else:
                    break
        # find even palindrome
        for i in range(len(s)):
            j = 1
            while i - j + 1 >= 0 and i + j < len(s):
                if s[i - j + 1] == s[i + j]:
                    if 2 * j > len(longest):
                        longest = s[i - j + 1:i + j + 1]
                    j += 1
                else:
                    break
        return longest


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_length = max(len1, len2)
            if end - start + 1 < max_length:
                start = i - (max_length - 1) // 2
                end = i + max_length // 2
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == "__main__":
    # doctest.testmod(verbose=True)
    # sol = Solution()
    # print(sol.longestPalindrome('babad'))
    # print(sol.longestPalindrome('bb'))
    # print(sol.longestPalindrome('cbba'))
    # print(sol.longestPalindrome('qabbap'))
    sol2 = Solution2()
    print(sol2.longestPalindrome('babad'))
    print(sol2.longestPalindrome('babad'))
    print(sol2.longestPalindrome('cbba'))
    print(sol2.longestPalindrome('cbba'))
