from typing import List
from collections import defaultdict


class Solution:
    """
    Runtime: 688 ms, faster than 82.35% of Python3 online submissions for Maximum Equal Frequency.
    Memory Usage: 21.6 MB, less than 38.82% of Python3 online submissions for Maximum Equal Frequency.
    """
    def maxEqualFreq(self, nums: List[int]) -> int:
        def default_count():
            return 0

        def works():
            # this function should have a time complexity of O(1)
            type_count_size = len(type_count)
            if type_count_size > 2:
                return False
            elif type_count_size == 1:
                # [1], [1,2], [1,2,3], [1,1,2,2]
                if list(type_count.values())[0] == 1:  # O(1)
                    # [1,1,1]
                    return True
                return list(type_count.keys())[0] == 1  # [1,1,2,2] will fail, [1,2,3,4] will pass, O(1)
            else:  # len(type_count_keys) == 2
                # e.g. [1,1,2,2,3]
                # e.g. [1,1,2,2,3,3,3]
                count_2_items = list(type_count.items())  # O(1)
                if count_2_items[0][1] == 1:
                    if count_2_items[0][0] - count_2_items[1][0] == 1 or count_2_items[0][0] == 1:
                        return True
                elif count_2_items[1][1] == 1:
                    if count_2_items[1][0] - count_2_items[0][0] == 1 or count_2_items[1][0] == 1:
                        return True
                return False

        freq = defaultdict(default_count)  # keeps track of frequency, [1,2,2,3,3,3] -> freq = {1:1, 2:2, 3:3}
        type_count = defaultdict(default_count)  # freq of freq, [1,2,2,3,3,4,4,4] -> type_count = {1: 1, 2: 2, 3: 1}
        best_so_far = 0  # longest prefix so far
        for i in range(len(nums)):
            freq[nums[i]] += 1
            type_count[freq[nums[i]]] += 1
            cur_freq = freq[nums[i]]
            if cur_freq != 1:
                # if current freq is 1, previous freq is 0, didn't exist, then no need to decrement type_count
                type_count[cur_freq - 1] -= 1  # decrement previous frequency type
                if type_count[cur_freq - 1] == 0:
                    type_count.pop(cur_freq - 1)
            if works():
                best_so_far = i + 1
        return best_so_far


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxEqualFreq([2, 2, 1, 1, 5, 3, 3, 5]) == 7
    assert sol.maxEqualFreq([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]) == 13
