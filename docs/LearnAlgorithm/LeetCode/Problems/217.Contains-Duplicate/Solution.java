/**
 * Runtime: 6 ms, faster than 66.08% of Java online submissions for Contains Duplicate.
 * Memory Usage: 45.6 MB, less than 61.42% of Java online submissions for Contains Duplicate.
 * Using set or hash map to record what number has been seen, if the same number appears again, can be detected in O(1) time
 * Time Complexity: O(n)
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for(int num : nums) {
            if (set.contains(num))
                return true;
            else
                set.add(num);
        }
        return false;
    }
}