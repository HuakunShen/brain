#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.size(); i++)
            maxprofit += max(prices[i] - prices[i - 1], 0);
        return maxprofit;
    }
};

int main() {
    Solution sol;
    std::vector<int> prices = {7, 1, 5, 3, 6, 4};
    assert(sol.maxProfit(prices) == 7);

    prices = {1, 2, 3, 4, 5};
    assert(sol.maxProfit(prices) == 4);

    prices = {7, 6, 4, 3, 1};
    assert(sol.maxProfit(prices) == 0);

    cout << "All Correct" << endl;
}