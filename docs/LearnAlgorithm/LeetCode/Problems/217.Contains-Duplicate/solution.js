/**
 * Runtime: 80 ms, faster than 88.31% of JavaScript online submissions for Contains Duplicate.
 * Memory Usage: 42.8 MB, less than 59.51% of JavaScript online submissions for Contains Duplicate.
 *
 * Using set or hash map to record what number has been seen, if the same number appears again, can be detected in O(1) time
 * Time Complexity: O(n)
 *
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const set = new Set();
    for (let i = 0; i < nums.length; i++) {
        if (set.has(nums[i])) return true
        else set.add(nums[i])
    }
    return false
};