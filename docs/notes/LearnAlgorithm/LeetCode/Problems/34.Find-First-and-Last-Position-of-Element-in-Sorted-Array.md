# 34. Find First and Last Position of Element in Sorted Array

Level: Medium

Although the level is medium, I feel like it's Easy.


Two ways to do this
1. run 2 iterations, forward and backward, find the first occurence of target
2. Run a single loop, use a indicator to indicate whether it's searching for the first occurence or last
    If found first occurence, set `first`
    If during the process of find

Both have a time complexity of O(n), space complexity of O(1) if we ignore the input variable, only 4 integers used.


```python
class Solution:
    """
    Runtime: 146 ms, faster than 24.75% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 15.3 MB, less than 94.37% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mode = 1
        first, last = -1, -1
        for i in range(len(nums)):
            if mode == 1:
                if nums[i] == target:
                    mode = 2
                    first = i
                    last = i
            else:
                # model == 2
                if nums[i] == target:
                    last = i
        return first, last
```