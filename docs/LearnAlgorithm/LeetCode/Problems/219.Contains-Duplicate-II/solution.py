from typing import List


class Solution:
    """
    Runtime: 100 ms, faster than 60.47% of Python3 online submissions for Contains Duplicate II.
    Memory Usage: 21.6 MB, less than 34.55% of Python3 online submissions for Contains Duplicate II.
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table and abs(i - table[nums[i]]) <= k:
                return True
            table[nums[i]] = i
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))
