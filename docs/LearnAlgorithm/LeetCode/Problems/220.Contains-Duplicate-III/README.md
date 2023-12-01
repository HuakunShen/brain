# 219. Contains Duplicate III

[Problem](https://leetcode.com/problems/contains-duplicate-iii/)

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between **nums[i]** and **nums[j]** is at most t and the absolute difference between i and j is at most k.

> Runtime: 31 ms, faster than 31.05% of Java online submissions for Contains Duplicate III.
> Memory Usage: 41.2 MB, less than 29.07% of Java online submissions for Contains Duplicate III.

Time Complexity: O(n log n)

## Java Implementation

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> set = new TreeSet<>();
            for (int i = 0; i < nums.length; ++i) {
                Long ceil = set.ceiling((long) nums[i]);
                if (ceil != null && ceil - nums[i] <= t) {
                    return true;
                }

                Long floor = set.floor((long) nums[i]);
                if (floor != null && nums[i] - floor <= t) {
                    return true;
                }

                set.add((long) nums[i]);
                if (set.size() > k) {
                    set.remove((long) nums[i - k]);
                }
            }
            return false;
    }
}
```

## Python Implementation

```python
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

```