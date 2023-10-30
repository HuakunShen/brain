# 220. Contains Duplicate III
from typing import List
import doctest


class Solution0:
    """
    Brute Force Approach
    Time Limit Exceeded
    Time Complexity: O(n^2)
    """

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        >>> sol=Solution0()
        >>> print(sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
        True
        >>> print(sol.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
        True
        >>> print(sol.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
        False
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and abs(i - j) <= k and abs(nums[i] - nums[j]) <= t:
                    return True
        return False


class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        pass


if __name__ == '__main__':
    doctest.testmod(verbose=True)
