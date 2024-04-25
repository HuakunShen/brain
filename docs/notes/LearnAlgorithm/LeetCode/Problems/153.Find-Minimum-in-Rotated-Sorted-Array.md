# 153. Find Minimum in Rotated Sorted Array

## Explanation

### Intro

The trick is to understand the property of rotation.

Since the original array is in order, if we pick a starting point (s), a mid point (mid) and a end point (e),
their values must be in sorted order: (low, medium, high), let's denote this by (1, 2, 3).

Rotating The array doesn't change the property, and the entire array can be simplified to the 3 numbers, let's call them the 3 pillars.

Suppose the original array is [1, 2, 3, 4, 5, 6, 7], then the 3 pillars are (1, 4, 7), and their order size order (1, 2, 3). No matter how to rotate, the order will be one of the following

- (1, 2, 3)
- (3, 1, 2)
- (2, 3, 1)

Which are all the rotations of (1, 2, 3).

Another property is that, the smallest number is always between size order 1 and 3 (i.e. low and high).

Consider the following example [4, 5, 6, 7, 0, 1, 2].

s = 4, mid = 7, e = 2. The size order is (2, 3, 1), the smallest number in this array is 0 and is between mid and e (i.e. size order 3 and 1).

### Conclusion

Binary Search will be the core of the algorithm, where half of the candidates are purged in each iteration.

We need to guarantee that the half we search must contain the lowest value. I already discussed the property of rotated sorted array, so we always want to search in the direction between low and high (1 and 3).

We just need to check which of the 3 cases current state falls in.

- (1, 2, 3) -> already know the answer
- (3, 1, 2) -> search left
- (2, 3, 1) -> search right

And search in the direction between 1 and 3.

Size order (1, 2, 3) is a special case, in this case, we already know the answer, `nums[s]` is the lowest value.

## Solution

**Time Complexity:** O(n)

### Solution 1

```python
class Solution:
    """
    Runtime: 40 ms, faster than 94.17% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
    Memory Usage: 14.2 MB, less than 27.62% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
    """
    def findMin(self, nums: List[int]) -> int:
        s, e, lowest_so_far = 0, len(nums) - 1, float("inf")
        while s <= e:
            mid = (s + e) // 2
            lowest_so_far = min(lowest_so_far, nums[s], nums[mid], nums[e])
            if nums[mid] < nums[s] and nums[mid] < nums[e]:
                # search in left part
                e = mid - 1
            elif nums[mid] > nums[s] and nums[mid] > nums[e]:
                # search in right part
                s = mid + 1
            else:
                # nums[s] < nums[mid] < nums[e], nums[s] < nums[mid] < nums[e], nums[s] is the lowest and is already taken into account by lowest_so_far
                break
        return lowest_so_far
```

### Solution 2

A simpler solution: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/1912836/Very-clear-and-elegant-solution-with-explanation

```python
class Solution:
    """
    Runtime: 36 ms, faster than 98.20% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
    Memory Usage: 14.3 MB, less than 27.62% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

    """
    def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums) - 1
        while r > l + 1:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m
            else:
                r = m
        return nums[r]
```

## Test Cases

```
[1,2]
[2,1]
[3,1,2]
[3,4,5,1,2]
[4,5,6,7,0,1,2]
[11,13,15,17]
[6,7,8,1,2,3,4,5]
```
