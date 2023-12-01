# 121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

This is a greedy algorithm question.

Iterate through the list, and calculate the best solution for now, record the best solution so far, go to the next price and continue.

The idea is, the current best solution is either the **difference between the current price and the lowest price in previous prices**, or the previous best solution. 

This is a bellman equation.

[solution.py](./solution.py)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        prev_sol = 0 if prices[1] <= prices[0] else prices[1] - prices[0]
        min_num = min(prices[:2])
        for i in range(2, len(prices)):
            cur_num = prices[i]
            prev_sol = max(cur_num - min_num, prev_sol)
            min_num = min(min_num, cur_num)
        return prev_sol
```