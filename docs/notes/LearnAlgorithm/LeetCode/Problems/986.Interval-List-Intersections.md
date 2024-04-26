# 986. Interval List Intersections

https://leetcode.com/problems/interval-list-intersections/

Level: Medium, should be Easy

## Solution

### Complexity

> Runtime: 177 ms, faster than 67.57% of Python3 online submissions for Interval List Intersections.
>
> Memory Usage: 14.9 MB, less than 53.51% of Python3 online submissions for Interval List Intersections.

Suppose `firstList` has length=`N`, `secondList` has length=`M`.

#### Time Complexity

`O(N+M)`: checking and calculating intersection takes constant time. Simply iterate through both lists.

#### Space Complexity

`O(1)` without considering the space to store result and inputs.

The result list takes `O(N+M)` space.

### Idea

1. Starting from the first interval in both list
2. If there is a intersection, record it
3. Compare the upper interval bound of two current intervals.
   1. The interval with smaller upper bound will move forward because the next interval of the list could potentially intersect with the unmoved interval.

```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        has_intersection = lambda interval1, interval2: (min(interval1[1], interval2[1]) - max(interval1[0], interval2[0])) >= 0
        get_intersection = lambda interval1, interval2: [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
        len1, len2 = len(firstList), len(secondList)
        f_ptr, s_ptr = 0, 0     # first pointer and second pointer
        intersections = []
        while f_ptr < len1 and s_ptr < len2:
            f, s = firstList[f_ptr], secondList[s_ptr]
            if has_intersection(f, s):
                intersections.append(get_intersection(f, s))
            if f[1] < s[1] and f_ptr < len1:
                f_ptr += 1
            else:
                s_ptr += 1
        return intersections
```
