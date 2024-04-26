# 31. Next Permutation

https://leetcode.com/problems/next-permutation/

Level: Medium (quite complicated, have to draft and think many cases and find the pattern)

## Solution (My Initial Solution)

Since sorted function is used, the time complexity is O(n log n)

```python
class Solution:
		"""
		Runtime: 44 ms, faster than 87.74% of Python3 online submissions for Next Permutation.
		Memory Usage: 13.9 MB, less than 79.00% of Python3 online submissions for Next Permutation.
		"""
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1,2,3,4] -> [1,2,4,3]
        [1,4,2,3] -> [1,4,3,2]
        [1,6,2,3,4,5] -> [1,6,2,3,5,4]
        [1,6,2,5,4,3] -> [1,6,3,2,4,5]
        [1,6,2,5,3,4] -> [1,6,2,5,4,3]
        [3,2,1] -> [1,2,3]
        [6,4,2,5,3,1] -> [6,4,3,1,2,5]
        [2,5,3,1] -> [3,1,2,5]
        iterate backwards, find the the longest reverse numbers possible
        
        """
        def shift_inplace(arr, start_idx, num_2_shift, space_2_shift=1):
            for i in range(start_idx + num_2_shift - 1, start_idx - 1, -1):
                arr[i + space_2_shift] = arr[i]
                
        def replace(arr, target, start_idx):
            """Replace elements in arr to target starting at start_idx"""
            for i in range(len(target)):
                arr[i + start_idx] = target[i]
        
        last_idx = len(nums) - 1
        i = last_idx
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1    
        if i == 1 and nums[0] > nums[1]:
            replace(nums, sorted(nums), 0)
        else:
            p1, p2 = i - 1, last_idx
            for i in range(last_idx, p1, -1):
                if nums[p1] < nums[i]:
                    p2 = i  # p2 will be moved forward
                    break
            p1_num, p2_num = nums[p1], nums[p2]
            shift_inplace(nums, p1, p2 - p1, 1)
            nums[p1] = p2_num
            if p1_num < p2_num:
                replace(nums, sorted(nums[p1 + 1:]), p1 + 1)
        
```

## Solution (My implementation of official solution)

After reading the official solution, I found that it's quite similar to my original solution.

It's faster because it doesn't need to sort anything, instead reverse is enough (which I didn't realize).


The point of sorting is that, after swapping, we want `nums[p1 + 1:]` to become the smallest permutation. This is described in official solution.

Then I sorted `nums[p1 + 1:]`.

The resulting subarray (`nums[p1:]`) must be in reverse order by designed. The `p2` by definition should be the idx of the first number greater than `nums[p1]` when searching backwards. So no need to sort. Just reverse.

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1,2,3,4] -> [1,2,4,3]
        [1,4,2,3] -> [1,4,3,2]
        [1,6,2,3,4,5] -> [1,6,2,3,5,4]
        [1,6,2,5,4,3] -> [1,6,3,2,4,5]
        [1,6,2,5,3,4] -> [1,6,2,5,4,3]
        [3,2,1] -> [1,2,3]
        [6,4,2,5,3,1] -> [6,4,3,1,2,5]
        [2,5,3,1] -> [3,1,2,5]
        iterate backwards, find the the longest reverse numbers possible
        
        """
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        def reverse(arr, start, end):
            copy = arr[start:end]
            count = start
            for i in range(len(copy) - 1, -1, -1):
                arr[count] = copy[i]
                count += 1
                
        last_idx = len(nums) - 1
        i = last_idx
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1    
        if i == 0:
            # Entire nums is in reverse order, just reverse again
            reverse(nums, 0, last_idx + 1)
        else:
            p1, p2 = i - 1, last_idx
            for i in range(last_idx, p1, -1):
                if nums[p1] < nums[i]:
                    p2 = i  # p2 will be moved forward
                    break
            swap(nums, p1, p2)
            reverse(nums, p1 + 1, last_idx + 1)
```

## Test Cases

```
[2,5,3,1]
[1,2,3]
[2,3,1]
[3,2,1]
[1,2,3,4]
[1,6,2,3,4,5]
[1,6,2,5,4,3]
[1,6,2,5,3,4]
[6,4,2,5,3,1]
```