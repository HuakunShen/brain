# 33. Search in Rotated Sorted Array

Level: Medium

## Solution

```python
class Solution:
    """
    Binary Search can be performed on a sorted array.
    To achieve O(log n), I have to use something like binary search
    
    Binary search uses a start and an end pointer. End should be always greater than start when nums are sorted. 
    This algo is a variant of binary search.
    A midpoint divides `nums` into 2 parts. One of them must be in order, the other may or may not (if no rotation at all, then both are in order).
    If target is in the range of the part in order, then perform a regular binary search.
    Otherwise, search the other part. 
    Repeat until there is no more numbers to search for.
    """
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        m = (s + e) // 2
        if nums[s] == target:
            # special case when len(nums) == 1
            return s
        while s < e:
            m = (s + e) // 2
            print(s, m, e)
            if nums[e] == target:
                # when calculating mid point, it will always round down that `m` would never be `e`. Have to test it separately
                return e
            if nums[m] == target:
                return m
            if nums[s] == target:
                return s
            if nums[s] < nums[m]:
                # left section in order, right out order
                if nums[s] < target < nums[m]:
                    # regular binary search in left section
                    e = m - 1
                else: # search right section
                    s = m + 1
            else:
                # right section in order
                if nums[m] < target < nums[e]:
                    # regular binary search in right section
                    s = m + 1
                else: # search left section
                    e = m - 1
        return -1                
```

## Test Cases

```
[4,5,6,7,0,1,2]
0
[1]
0
[1]
1
[1,3,5]
1
[4,5,6,7,0,1,2]
1
[1,3]
2
```