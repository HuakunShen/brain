# 162. Find Peak Element

## Solution

[Official Solution](https://leetcode.com/problems/find-peak-element/solution/)

### Linear Search

O(n)

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        else:
            for i in range(len(nums)):
                if i == 0 and nums[0] > nums[1]:
                    return 0
                if i == len(nums) - 1 and nums[-1] > nums[-2]:
                    return len(nums) - 1
                if nums[i] > nums[i] - 1 and nums[i] > nums[i + 1]:
                    return i
```

### Another Lineary Search

Unlike the previous method which explicitly listed all conditions. This method implicitly considers all scenarios, including edge cases. 

Iterate and always check if current is higher than the next number. 

If not higher, then it's incrementing, keep going, in the worst case, if it increments to the end, return the last index. 

If higher it's now higher than the previous and next number, because, by definition, current number is higher than all previous numbers.

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1
```

### Iterative Binary Search

Time Complexity: O(log2 n)

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                # search left
                r = m
            else:
                l = m + 1
        return l
```

## Test Cases

```
[1,2,3,1]
[1,2,1,3,5,6,4]
[2,1]
[1,2]
[6,5,4,3,2,3,2]
```