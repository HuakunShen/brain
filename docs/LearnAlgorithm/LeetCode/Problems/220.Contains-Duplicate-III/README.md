# 219. Contains Duplicate III

[Problem](https://leetcode.com/problems/contains-duplicate-iii/)

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between **nums[i]** and **nums[j]** is at most t and the absolute difference between i and j is at most k.

> Runtime: 31 ms, faster than 31.05% of Java online submissions for Contains Duplicate III.
> Memory Usage: 41.2 MB, less than 29.07% of Java online submissions for Contains Duplicate III.

Time Complexity: O(n log n)

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