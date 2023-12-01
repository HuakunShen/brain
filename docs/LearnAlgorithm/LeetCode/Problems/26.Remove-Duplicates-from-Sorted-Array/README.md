# 26. Remove Duplicates from Sorted Array

Time Complexity: O(n)
Space Complexity: O(1)

Double Pointers (index), i for updating unique numbers, j for skipping duplicate numbers.

Once j finds a new number, set the number to position i and move i to the next position

## Python Solution

> Runtime: 84 ms, faster than 61.54% of Python3 online submissions for Remove Duplicates from Sorted Array.
> Memory Usage: 16 MB, less than 51.79% of Python3 online submissions for Remove Duplicates from Sorted Array.

```python
# 26. Remove Duplicates from Sorted Array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 1
        pre_val = nums[0]
        while index < len(nums):
            if nums[index] == pre_val:
                nums.pop(index)
            else:
                pre_val = nums[index]
                index += 1
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1
        
    def removeDuplicates3(self, nums: List[int]) -> int:
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates2([1, 1, 2]))
```

## Golang Solution

```go
func removeDuplicates(nums []int) int {
    i := 0
    for j := 1; i < len(nums) && j < len(nums); j++ {
        if nums[i] != nums[j]{
            i += 1
            nums[i] = nums[j]
        }
    }
    return i + 1
}
```
