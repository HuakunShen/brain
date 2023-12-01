# 219. Contains Duplicate II

[Problem](https://leetcode.com/problems/contains-duplicate-ii/)

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that **nums[i] = nums[j]** and the absolute difference between i and j is at most k.

## Related Problems

### 217. Contains Duplicate
[LeetCode](https://leetcode.com/problems/contains-duplicate/)

[Solution](../217.Contains-Duplicate/README.md)

### 219. Contains Duplicate III

[LeetCode](https://leetcode.com/problems/contains-duplicate-iii/)

<!-- [Solution](../217.Contains-Duplicate-III) -->


# Solution

> Runtime: 100 ms, faster than 60.47% of Python3 online submissions for Contains Duplicate II.
> Memory Usage: 21.6 MB, less than 34.55% of Python3 online submissions for Contains Duplicate II.

Similar Algorithm to [217. Contains Duplicate](../217.Contains-Duplicate/README.md), using set.

One iteration through the list is enough.

Since the difference can be at most k, so we can update the index whenever we see a new occurrence. 

Time Complexity: O(n)

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table and abs(i - table[nums[i]]) <= k:
                return True
            table[nums[i]] = i
        return False
```