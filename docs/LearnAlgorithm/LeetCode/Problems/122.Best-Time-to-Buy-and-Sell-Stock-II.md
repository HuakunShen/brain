# 122. Best Time to Buy and Sell Stock II

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

The idea is 低买高卖, buy in the valley and sell at the peak.

- [CPP Solution](./solution.cpp)

## Idea

1. Start from the beginning, loop throught the prices array
2. Find the next valley and sell at the next peak

The idea can be simplified to the following code.

```cpp
int maxProfit(vector<int> &prices) {
    int maxprofit = 0;
    for (int i = 1; i < prices.size(); i++)
        maxprofit += max(prices[i] - prices[i - 1], 0);
    return maxprofit;
}
```

While looking for the next valley, 0 is always added to `maxprofit`.

While looking for the next peak, it will accumulate the differences.

Time Complexity: $O(n)$

Space Complexity: $O(1)$
