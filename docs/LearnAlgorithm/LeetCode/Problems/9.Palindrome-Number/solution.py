import doctest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        >>> sol = Solution()
        >>> sol.isPalindrome(121)
        True
        >>> sol.isPalindrome(-121)
        False
        >>> sol.isPalindrome(10)
        False
        """
        x_str = str(x)
        for i in range(len(x_str)):
            if x_str[i] != x_str[-(i + 1)]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        """
        >>> sol = Solution()
        >>> sol.isPalindrome(121)
        True
        >>> sol.isPalindrome(-121)
        False
        >>> sol.isPalindrome(10)
        False
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse = 0
        while x > reverse:
            reverse *= 10
            reverse += x % 10
            x = x // 10

        if x == reverse or x == reverse // 10:
            return True
        return False


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    # sol = Solution()
    # print(sol.isPalindrome(121))
    # print(sol.isPalindrome(-121))
    # print(sol.isPalindrome(10))
