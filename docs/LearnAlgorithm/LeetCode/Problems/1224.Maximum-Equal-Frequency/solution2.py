from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 404 ms, faster than 100.00% of Python3 online submissions for Maximum Equal Frequency.
    Memory Usage: 21.4 MB, less than 96.47% of Python3 online submissions for Maximum Equal Frequency.
    """

    def maxEqualFreq(self, nums: List[int]) -> int:
        count = Counter(nums)
        valuesCount = Counter(count.values())

        for i in range(len(nums) - 1, -1, -1):
            if len(valuesCount) == 2:
                if (max(valuesCount.keys()) - 1 == min(valuesCount.keys())) and (
                        valuesCount[max(valuesCount.keys())] == 1):
                    # valuesCount = {2: 1, 1: 1}, {9: 1, 8: 10}
                    return i + 1
                if valuesCount[min(valuesCount.keys())] == 1 and min(valuesCount.keys()) == 1:
                    # valuesCount = {1: 1, 5: 6}
                    return i + 1
            elif len(count) == 1:
                # [1,1,1,1,1]
                return i + 1
            elif len(valuesCount) == 1 and 1 in valuesCount:
                # nums = [1,2,3,4,5] -> valuesCount = {1: 5}
                return i + 1
            cur_num = nums[i]
            c = count[cur_num]
            valuesCount[c] -= 1
            if c - 1 != 0:
                valuesCount[c - 1] += 1
            count[cur_num] -= 1
            if count[cur_num] == 0:
                count.pop(cur_num)
            if valuesCount[c] == 0:
                valuesCount.pop(c)


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxEqualFreq([2, 2, 1, 1, 5, 3, 3, 5]) == 7
