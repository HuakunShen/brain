# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        >>> sol = Solution()
        >>> sol.maxProfit([1, 4, 2])
        3
        """
        if len(prices) < 2:
            return 0
        prev_sol = 0 if prices[1] <= prices[0] else prices[1] - prices[0]
        min_num = min(prices[:2])
        for i in range(2, len(prices)):
            cur_num = prices[i]
            prev_sol = max(cur_num - min_num, prev_sol)
            min_num = min(min_num, cur_num)
        return prev_sol

if __name__ == '__main__':
    import doctest
    doctest.testmod()