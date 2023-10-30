// 220. Contains Duplicate III

/**
 * Runtime: 31 ms, faster than 31.05% of Java online submissions for Contains Duplicate III.
 * Memory Usage: 41.2 MB, less than 29.07% of Java online submissions for Contains Duplicate III.
 * Time Complexity: O(n log n)
 */
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