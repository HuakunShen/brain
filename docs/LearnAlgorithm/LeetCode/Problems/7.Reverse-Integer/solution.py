import doctest


class Solution:
    def reverse(self, x: int) -> int:
        """
        >>> sol = Solution()
        >>> sol.reverse(123)
        321
        >>> sol.reverse(-123)
        -321
        >>> sol.reverse(1534236469)
        0
        """
        result = ""
        string = str(x)
        if x < 0:
            result += "-"
            string = string[1:]
        for i in range(len(string) - 1, -1, -1):
            result += string[i]
        result_int = int(result)
        if result_int > 2 ** 31 - 1 or result_int < -2 ** 31:
            result_int = 0
        return result_int

    def reverse2(self, x: int) -> int:
        """
        >>> sol = Solution()
        >>> sol.reverse2(123)
        321
        >>> sol.reverse2(-123)
        -321
        >>> sol.reverse2(1534236469)
        0
        """
        copy = x
        result = 0
        if copy < 0:
            copy = copy * -1
        while copy != 0:
            result += copy % 10
            result *= 10
            copy = copy // 10
        result /= 10
        if x < 0:
            result = result * -1
        if result > 2 ** 31 - 1 or result < -2 ** 31:
            return 0
        return int(result)


if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    sol = Solution()
    print(sol.reverse2(-123))
