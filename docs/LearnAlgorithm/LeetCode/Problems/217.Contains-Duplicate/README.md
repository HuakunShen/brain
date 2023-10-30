# 217. Contains Duplicate

[Problem](https://leetcode.com/problems/contains-duplicate/)

## Solutions

[OfficialSolution](https://leetcode.com/problems/contains-duplicate/solution/)

[Python Solution](./solution.py)

[JavaScript Solution](./solution.js)

[Java Solution](./Solution.java)

[CPP Solution](./solution.cpp)

## Approach 1: Brute Force

Time Complexity: O(n^2)

Double loop, cross product, compare every pair or numbers

```python
class Solution0:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Double loop, cross product, compare every pair"""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False
```

## Approach 2: Sorting

> Runtime: 132 ms, faster than 58.36% of Python3 online submissions for Contains Duplicate.
> Memory Usage: 19 MB, less than 91.69% of Python3 online submissions for Contains Duplicate.

Sort first then detect if neighbor elements are the same    

Time Complexity: O(n*log n)

```python
class Solution1:

    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True
        return False
```

## Approach 3: Set/Hash Map

> Runtime: 124 ms, faster than 86.19% of Python3 online submissions for Contains Duplicate.
> Memory Usage: 18.9 MB, less than 97.11% of Python3 online submissions for Contains Duplicate.

Using set or hash map to record what number has been seen, if the same number appears again, can be detected in O(1) time
  
Time Complexity: O(n)

```python
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for num in nums:
            if num in set_:
                return True
            else:
                set_.add(num)
        return False
```